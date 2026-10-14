#!/bin/bash
# -----------------------------------------------------------------------
# sync_from_github.sh — 맥북에서 15분마다 실행 (cron)
#   1) Obsidian에서 고친 내용(교정 요청, 별표 등)을 GitHub에 올리고
#   2) 서버가 업데이트한 위키를 받아옵니다.
# 맥북이 깨어 있을 때만 돌고, 할 일이 없으면 아무것도 하지 않습니다.
# -----------------------------------------------------------------------
export PATH="/usr/local/bin:/opt/homebrew/bin:$PATH"
cd "$(dirname "$0")" || exit 1
mkdir -p logs

notify() {
    osascript -e "display notification \"$2\" with title \"$1\"" 2>/dev/null || true
}

{
    # 웹페이지용 자동 생성 파일은 서버가 다시 만드므로, 맥북 쪽 변경은 버림
    git checkout -- website/index.html data/papers.json data/topics.json 2>/dev/null

    # Obsidian에서 고친 내용이 있으면 기록
    if [ -n "$(git status --porcelain -- obsidian_notes)" ]; then
        echo "== $(date '+%F %T') Obsidian 수정 내용 기록"
        git add -- obsidian_notes
        git commit -q -m "맥북 Obsidian 수정 $(date +%F)"
    fi

    # 서버 쪽 업데이트 받아오기
    if ! git pull --rebase --autostash -q; then
        echo "== $(date '+%F %T') 받아오기 실패 (충돌)"
        git rebase --abort 2>/dev/null
        notify "논문 위키 - 동기화 충돌" "logs/sync.log 확인 필요"
        exit 1
    fi

    # 올릴 게 있으면 올리기
    if [ -n "$(git log '@{u}..HEAD' --oneline 2>/dev/null)" ]; then
        echo "== $(date '+%F %T') GitHub에 올리기"
        git push -q || notify "논문 위키 - 업로드 실패" "logs/sync.log 확인 필요"
    fi
} >> logs/sync.log 2>&1
