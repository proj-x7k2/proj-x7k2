#!/bin/bash
# -----------------------------------------------------------------------
# ask.sh — 위키에 질문하기
#   ./ask.sh "개 IVDD에서 MRI와 CT 비교 근거 정리해줘"
# 위키에 쌓인 논문을 근거로 답하고, 다시 볼 가치가 있는 답은
# obsidian_notes/queries/ 에 저장됩니다.
# (대화하듯 여러 번 묻고 싶으면 이 폴더에서 그냥 `claude` 를 실행해도 됩니다.
#  CLAUDE.md의 질의 워크플로우를 자동으로 따릅니다.)
# -----------------------------------------------------------------------
source "$(dirname "$0")/common.sh"
if [ -z "$1" ]; then
    echo '사용법: ./ask.sh "질문 내용"'
    exit 1
fi
LOG_FILE="logs/$(date +%Y-%m-%d_%H-%M)-ask.log"
load_token
run_claude "CLAUDE.md의 '워크플로우 C — 질의'를 따라 다음 질문에 답해줘: $1"
python3 build_site.py > /dev/null 2>&1 || true
