#!/bin/bash
# -----------------------------------------------------------------------
# common.sh — 다른 스크립트들이 공통으로 불러 쓰는 설정입니다. 직접 실행하지 않습니다.
# -----------------------------------------------------------------------

# cron은 최소한의 PATH로 실행되어 nvm으로 설치한 claude, python.org 파이썬 등을
# 못 찾습니다. 터미널에서 직접 실행할 때와 같은 환경이 되도록 경로를 보충합니다.
export PATH="/usr/local/bin:/opt/homebrew/bin:$HOME/.local/bin:$PATH"
if [ -s "$HOME/.nvm/nvm.sh" ]; then
    . "$HOME/.nvm/nvm.sh" > /dev/null 2>&1 || true
fi

set -e
set -E            # 함수 안에서 난 오류도 오류 알림(trap)이 잡도록
set -o pipefail   # 파이프(| tee) 앞 명령의 실패도 놓치지 않도록

cd "$(dirname "$0")"
mkdir -p logs

# Claude Code에 허용할 도구: 읽기/쓰기/수정 + 폴더 둘러보기(Glob) + 내용 검색(Grep)
CLAUDE_TOOLS="Read,Write,Edit,Glob,Grep"

notify() {
    osascript -e "display notification \"$2\" with title \"$1\"" 2>/dev/null || true
}

log() {
    echo "$1" | tee -a "$LOG_FILE"
}

check_tools() {
    if ! command -v claude > /dev/null 2>&1; then
        log "오류: claude 명령을 찾을 수 없습니다 (PATH: $PATH)"
        notify "논문 위키 - 오류" "claude 명령을 찾을 수 없음"
        exit 1
    fi
}

load_token() {
    check_tools
    # 구독 계정으로만 실행되도록 API 키는 항상 제거
    unset ANTHROPIC_API_KEY
    if [ -f "claude_token.txt" ]; then
        export CLAUDE_CODE_OAUTH_TOKEN="$(cat claude_token.txt)"
    else
        log "오류: claude_token.txt 파일이 없습니다."
        notify "논문 위키 - 오류" "claude_token.txt 없음, 확인 필요"
        exit 1
    fi
}

run_claude() {
    # 사용법: run_claude "프롬프트 내용" [추가 허용 도구]
    local tools="$CLAUDE_TOOLS"
    if [ -n "$2" ]; then tools="$tools,$2"; fi
    claude -p "$1" --allowedTools "$tools" --permission-mode acceptEdits 2>&1 | tee -a "$LOG_FILE"
}

git_sync() {
    # GitHub 원격 저장소가 연결된 경우에만 커밋·푸시 (raw/ 는 .gitignore로 제외됨)
    if git remote get-url origin > /dev/null 2>&1; then
        log "--- GitHub 반영 ---"
        git add obsidian_notes data/papers.json data/topics.json website/index.html CLAUDE.md 2>&1 | tee -a "$LOG_FILE"
        if [ -f data/skipped.json ]; then git add data/skipped.json; fi
        if ! git diff --cached --quiet; then
            git commit -m "$1" 2>&1 | tee -a "$LOG_FILE"
            git push 2>&1 | tee -a "$LOG_FILE"
        else
            log "반영할 변경 사항 없음"
        fi
    fi
}
