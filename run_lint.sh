#!/bin/bash
# run_lint.sh — 위키 점검을 지금 바로 실행하고 싶을 때 (평소엔 매월 첫 주 자동 실행)
source "$(dirname "$0")/common.sh"
LOG_FILE="logs/$(date +%Y-%m-%d_%H-%M)-lint.log"
trap 'notify "논문 위키 - 오류" "점검 중 오류 발생 (로그: $LOG_FILE)"' ERR
load_token
log "=== $(date) 위키 점검 시작 ==="
run_claude "$(cat prompts/lint.txt)"
date +%Y-%m > data/last_lint.txt
python3 build_site.py 2>&1 | tee -a "$LOG_FILE"
git_sync "위키 점검 $(date +%Y-%m-%d)"
notify "논문 위키" "점검 완료 — obsidian_notes/lint-report.md 확인"
