#!/bin/bash
# -----------------------------------------------------------------------
# migrate_v2.sh — 기존 위키를 v2 구조로 한 번만 전환하는 스크립트
#   ./migrate_v2.sh
# 실행 전 현재 상태를 git에 백업 커밋하므로, 결과가 마음에 안 들면 되돌릴 수 있습니다.
# -----------------------------------------------------------------------
source "$(dirname "$0")/common.sh"
LOG_FILE="logs/$(date +%Y-%m-%d_%H-%M)-migrate.log"
trap 'notify "논문 위키 - 오류" "v2 전환 중 오류 (로그: $LOG_FILE)"' ERR
load_token

log "=== v2 전환 시작 ==="

# 0) 백업 커밋 (로컬만, push 안 함)
git add -A 2>&1 | tee -a "$LOG_FILE"
if ! git diff --cached --quiet; then
    git commit -m "v2 전환 직전 백업" 2>&1 | tee -a "$LOG_FILE"
fi
BACKUP_COMMIT=$(git rev-parse --short HEAD)
log "백업 커밋: $BACKUP_COMMIT"

# 1) 이제 추적하지 않을 파일을 git 추적에서 제외 (파일 자체는 그대로 둠)
git rm -r -q --cached --ignore-unmatch -- '*.DS_Store' 'obsidian_notes/.obsidian/workspace.json' 2>&1 | tee -a "$LOG_FILE"

# 더 이상 쓰지 않는 v1 파일 정리 (git 기록에는 남아 있음)
rm -f main.py summarize.py summarize_prompt.txt .env.example

# 2) 기존 논문들의 원자료를 raw/pubmed/ 에 채워넣기
log "--- 원자료 채워넣기 ---"
python3 fetch_papers.py --backfill 2>&1 | tee -a "$LOG_FILE"

# 3) Claude Code로 위키 형식 전환 (파일명 변경·옛 파일 삭제를 위해 rm 허용)
log "--- 위키 형식 전환 (Claude Code) ---"
run_claude "$(cat prompts/migrate_v2.txt)" "Bash(rm:*),Bash(mkdir:*)"

# 4) 처리 기록 정리 + 웹사이트 재생성
python3 fetch_papers.py --reconcile 2>&1 | tee -a "$LOG_FILE" || true
python3 build_site.py 2>&1 | tee -a "$LOG_FILE"

log "=== v2 전환 완료 ==="
log "Obsidian과 website/index.html 을 확인해보세요."
log "마음에 안 들면 되돌리기:  git reset --hard $BACKUP_COMMIT"
log "괜찮으면 GitHub 반영:     git add -A && git commit -m 'v2 전환' && git push"
notify "논문 위키" "v2 전환 완료 — 결과 확인 후 GitHub 반영하세요"
