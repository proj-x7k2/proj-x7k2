#!/bin/bash
# -----------------------------------------------------------------------
# run_weekly.sh — 매주 자동 실행 (cron)
#   1) PubMed 새 논문 수집 (비용 없음)
#   2) 새 논문 또는 새 PDF가 있으면 Claude Code로 위키에 반영 (10편씩 나눠 반복)
#   3) 반영이 확인된 논문만 "처리 완료" 표시 (중간에 멈춰도 다음 주 재시도)
#   4) 매월 첫 주에는 위키 점검(lint)도 함께 실행
#   5) 웹사이트 갱신 + GitHub 반영
# -----------------------------------------------------------------------
source "$(dirname "$0")/common.sh"
LOG_FILE="logs/$(date +%Y-%m-%d_%H-%M).log"
trap 'notify "논문 위키 - 오류" "실행 중 오류 발생 (로그: $LOG_FILE)"' ERR

log "=== $(date) 주간 실행 시작 ==="
load_token
python3 make_digest.py --snapshot

# ── 0단계: 사용자가 남긴 교정 요청 반영 ──
FEEDBACK_COUNT=$(python3 feedback.py --count)
if [ "$FEEDBACK_COUNT" -gt 0 ]; then
    log "--- 교정 요청 ${FEEDBACK_COUNT}건 반영 ---"
    run_claude "$(cat prompts/feedback.txt)"
fi

# ── 1~2단계: 10편씩 나눠서 수집 → 위키 반영을 반복 ──
MAX_ROUNDS=$(python3 -c "import config; print(config.MAX_ROUNDS)")
BATCH_SIZE=$(python3 -c "import config; print(config.MAX_RESULTS)")
TOTAL_DONE=0
ROUND=0
while [ "$ROUND" -lt "$MAX_ROUNDS" ]; do
    ROUND=$((ROUND + 1))
    log "--- [${ROUND}회차] 논문 검색 ---"
    python3 fetch_papers.py 2>&1 | tee -a "$LOG_FILE"

    NEW_COUNT=$(python3 -c "import json; print(len(json.load(open('data/raw_papers.json', encoding='utf-8'))))")
    PENDING_PDFS=$(python3 pdf_tracker.py --pending-count)
    log "이번 회차: 논문 ${NEW_COUNT}편 / 새 PDF ${PENDING_PDFS}개"

    if [ "$NEW_COUNT" -eq 0 ] && [ "$PENDING_PDFS" -eq 0 ]; then
        log "처리할 것이 없어 반복 종료"
        break
    fi

    log "--- [${ROUND}회차] 위키 반영 (Claude Code) ---"
    run_claude "$(cat prompts/ingest.txt)"
    FINISHED=$(python3 fetch_papers.py --reconcile 2>&1 | tee -a "$LOG_FILE" | sed -n 's/^FINISHED=//p')
    python3 pdf_tracker.py --mark-done 2>&1 | tee -a "$LOG_FILE"
    TOTAL_DONE=$((TOTAL_DONE + ${FINISHED:-0}))

    # 이번 회차에 하나도 끝내지 못했으면 같은 걸 반복하지 않도록 중단
    if [ "${FINISHED:-0}" -eq 0 ]; then
        log "이번 회차에 완료된 논문이 없어 반복 종료 (다음 실행 때 재시도)"
        break
    fi
    # 마지막 배치였으면 종료
    if [ "$NEW_COUNT" -lt "$BATCH_SIZE" ]; then
        break
    fi
done

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

# ── 4단계: 웹사이트 갱신 ──
log "--- 웹사이트 갱신 ---"
python3 build_site.py 2>&1 | tee -a "$LOG_FILE"

# ── 5단계: 주간 다이제스트 ──
DIGEST_COUNT=$(python3 make_digest.py --prepare)
if [ "$DIGEST_COUNT" -gt 0 ]; then
    log "--- 주간 다이제스트 작성 (새 논문 ${DIGEST_COUNT}편) ---"
    run_claude "$(cat prompts/digest.txt)" || log "다이제스트 작성 실패 — 기본 목록으로 대체"
    python3 make_digest.py --fallback 2>&1 | tee -a "$LOG_FILE"
    python3 make_digest.py --issue "${SITE_URL:-}"
fi

# ── 6단계: GitHub 반영 ──
git_sync "주간 위키 업데이트 $(date +%Y-%m-%d)"

log "=== $(date) 실행 완료 ==="
notify "논문 위키" "논문 ${TOTAL_DONE}편 처리 완료${LINT_NOTE} (자세한 내용: obsidian_notes/log.md)"
