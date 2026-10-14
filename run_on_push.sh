#!/bin/bash
# -----------------------------------------------------------------------
# run_on_push.sh — 맥북 Obsidian에서 고친 내용(교정 요청, 별표 등)이
# GitHub에 올라오면 서버가 자동으로 실행합니다.
#   - 교정 요청이 있으면 Claude가 바로 반영
#   - 웹페이지 다시 만들기 (별표 등 반영)
# -----------------------------------------------------------------------
source "$(dirname "$0")/common.sh"
LOG_FILE="logs/$(date +%Y-%m-%d_%H-%M)-push.log"
trap 'notify "논문 위키 - 오류" "수정 반영 중 오류 (로그: $LOG_FILE)"' ERR

log "=== $(date) 맥북 수정 반영 시작 ==="
FEEDBACK_COUNT=$(python3 feedback.py --count)
if [ "$FEEDBACK_COUNT" -gt 0 ]; then
    load_token
    log "--- 교정 요청 ${FEEDBACK_COUNT}건 반영 ---"
    run_claude "$(cat prompts/feedback.txt)"
fi
python3 build_site.py 2>&1 | tee -a "$LOG_FILE"
git_sync "맥북 수정 반영 $(date +%Y-%m-%d)"
log "=== $(date) 완료 ==="
