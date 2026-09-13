#!/bin/bash
# -----------------------------------------------------------------------
# run_weekly.sh
#
# 이 스크립트가 하는 일:
#   1) fetch_papers.py 실행 → PubMed에서 새 논문 확인 (비용 없음)
#   2) 새 논문이 있으면 Claude Code(headless 모드)에게 요약을 시킴
#      → CLAUDE_CODE_OAUTH_TOKEN(구독 계정 인증)만 사용하고,
#        ANTHROPIC_API_KEY는 절대 쓰지 않도록 명시적으로 비웁니다.
#        (API 키가 있으면 그쪽이 우선 적용되어 과금될 수 있기 때문)
#
# cron에 이 스크립트를 등록해두면 매주 자동으로 돌아갑니다.
# -----------------------------------------------------------------------

set -e  # 중간에 오류가 나면 즉시 멈춤

# 이 스크립트 파일이 있는 폴더로 이동 (cron은 기본 폴더가 다를 수 있어 필요함)
cd "$(dirname "$0")"

mkdir -p logs
LOG_FILE="logs/$(date +%Y-%m-%d_%H-%M).log"

echo "=== $(date) 실행 시작 ===" | tee -a "$LOG_FILE"

# ── 안전장치: API 키가 실수로 설정되어 있으면 비활성화 ──
# (구독 계정(OAuth) 대신 API 키가 있으면 그쪽으로 과금될 수 있으므로 항상 제거)
unset ANTHROPIC_API_KEY

# claude_token.txt 파일에 저장해둔 구독 인증 토큰을 불러옵니다.
if [ -f "claude_token.txt" ]; then
    export CLAUDE_CODE_OAUTH_TOKEN="$(cat claude_token.txt)"
else
    echo "오류: claude_token.txt 파일이 없습니다. README의 '완전 자동화 설정'을 먼저 진행하세요." | tee -a "$LOG_FILE"
    exit 1
fi

# ── 1단계: 새 논문 검색 (Claude 사용 안 함, 비용 없음) ──
echo "--- 1단계: 새 논문 검색 ---" | tee -a "$LOG_FILE"
python3 fetch_papers.py 2>&1 | tee -a "$LOG_FILE"

# ── 새 논문이 있는지 확인 ──
HAS_NEW=$(python3 -c "
import json
with open('data/raw_papers.json', encoding='utf-8') as f:
    papers = json.load(f)
print('yes' if papers else 'no')
")

if [ "$HAS_NEW" = "no" ]; then
    echo "새 논문이 없어 여기서 종료합니다." | tee -a "$LOG_FILE"
    exit 0
fi

# ── 2단계: Claude Code(headless)로 요약 생성 ──
echo "--- 2단계: 요약 생성 (Claude Code) ---" | tee -a "$LOG_FILE"
claude -p "$(cat summarize_prompt.txt)" \
    --allowedTools "Read,Write,Edit" \
    --permission-mode acceptEdits \
    2>&1 | tee -a "$LOG_FILE"

# ── 웹사이트 파일을 최신 데이터로 다시 생성 (서버 없이 더블클릭으로 열 수 있게) ──
echo "--- 웹사이트 파일 갱신 ---" | tee -a "$LOG_FILE"
python3 build_site.py 2>&1 | tee -a "$LOG_FILE"

# ── 3단계 (선택): 웹사이트 공유용 GitHub에 자동 반영 ──
# GitHub 원격 저장소(origin)가 실제로 연결되어 있을 때만 실행됩니다.
# (연결 안 했다면 이 프로젝트는 계속 로컬 전용으로만 동작하며, 이 단계는 조용히 건너뜁니다.)
if git remote get-url origin > /dev/null 2>&1; then
    echo "--- 3단계: GitHub에 새 내용 반영 (공유용 웹사이트 갱신) ---" | tee -a "$LOG_FILE"
    git add data/papers.json obsidian_notes/ website/index.html 2>&1 | tee -a "$LOG_FILE"
    if ! git diff --cached --quiet; then
        git commit -m "주간 논문 업데이트 $(date +%Y-%m-%d)" 2>&1 | tee -a "$LOG_FILE"
        git push 2>&1 | tee -a "$LOG_FILE"
    else
        echo "새로 반영할 변경 사항이 없습니다." | tee -a "$LOG_FILE"
    fi
fi

echo "=== $(date) 실행 완료 ===" | tee -a "$LOG_FILE"
