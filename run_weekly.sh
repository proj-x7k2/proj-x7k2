#!/bin/bash
# -----------------------------------------------------------------------
# run_weekly.sh — 매주 자동 실행 (cron)
#   1) PubMed 새 논문 수집 (비용 없음)
#   2) 새 논문 또는 새 PDF가 있으면 Claude Code로 위키에 반영 (수집 워크플로우)
#   3) 반영이 확인된 논문만 "처리 완료" 표시 (중간에 멈춰도 다음 주 재시도)
#   4) 매월 첫 주에는 위키 점검(lint)도 함께 실행
#   5) 웹사이트 갱신 + GitHub 반영
# -----------------------------------------------------------------------
source "$(dirname "$0")/common.sh"
LOG_FILE="logs/$(date +%Y-%m-%d_%H-%M).log"
trap 'notify "논문 위키 - 오류" "실행 중 오류 발생 (로그: $LOG_FILE)"' ERR

log "=== $(date) 주간 실행 시작 ==="
load_token

# ── 1단계: 새 논문 수집 ──
log "--- 1단계: 새 논문 검색 ---"
python3 fetch_papers.py 2>&1 | tee -a "$LOG_FILE"

NEW_COUNT=$(python3 -c "import json; print(len(json.load(open('data/raw_papers.json', encoding='utf-8'))))")
PENDING_PDFS=$(python3 pdf_tracker.py --pending-count)
log "처리할 새 논문: ${NEW_COUNT}편 / 새 PDF: ${PENDING_PDFS}개"

# ── 2단계: 위키 반영 ──
if [ "$NEW_COUNT" -gt 0 ] || [ "$PENDING_PDFS" -gt 0 ]; then
    log "--- 2단계: 위키 반영 (Claude Code) ---"
    run_claude "$(cat prompts/ingest.txt)"
    python3 fetch_papers.py --reconcile 2>&1 | tee -a "$LOG_FILE"
    python3 pdf_tracker.py --mark-done 2>&1 | tee -a "$LOG_FILE"
else
    log "새 논문·PDF 없음 — 위키 반영 단계 건너뜀"
fi

# ── 3단계: 매월 첫 주 점검 ──
THIS_MONTH=$(date +%Y-%m)
LAST_LINT=$(cat data/last_lint.txt 2>/dev/null || echo "")
if [ "$((10#$(date +%d)))" -le 7 ] && [ "$LAST_LINT" != "$THIS_MONTH" ]; then
    log "--- 3단계: 월간 위키 점검 ---"
    run_claude "$(cat prompts/lint.txt)"
    echo "$THIS_MONTH" > data/last_lint.txt
    LINT_NOTE=" · 월간 점검 완료"
else
    LINT_NOTE=""
fi

# ── 4단계: 웹사이트 갱신 + GitHub ──
log "--- 웹사이트 갱신 ---"
python3 build_site.py 2>&1 | tee -a "$LOG_FILE"
git_sync "주간 위키 업데이트 $(date +%Y-%m-%d)"

log "=== $(date) 실행 완료 ==="
notify "논문 위키" "새 논문 ${NEW_COUNT}편 확인${LINT_NOTE} (자세한 내용: obsidian_notes/log.md)"
