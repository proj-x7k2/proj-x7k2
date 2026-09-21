# 수의영상의학 논문 위키 (v2)

PubMed에서 소동물(개·고양이·토끼) 영상의학 논문을 매주 자동으로 모아, Claude Code가
주제별로 **누적되는 위키**(Obsidian)로 정리하고, 검색 가능한 아카이브 웹페이지를 만듭니다.

---

## 폴더 구조

| 경로 | 역할 | 직접 수정? |
|---|---|---|
| `CLAUDE.md` | 위키 관리 규칙(스키마). 주제 체계·형식·워크플로우 | 규칙을 바꾸고 싶을 때만 |
| `config.py` | 검색 조건 (영상 용어, 종, 기간 등) | 필요할 때 |
| `raw/pubmed/` | 논문 원자료 (자동 보관, 로컬 전용) | ✗ |
| `raw/pdf/` | 전문 PDF를 넣는 곳 | PDF 넣기만 |
| `obsidian_notes/` | 위키 본체 — Obsidian 볼트 | Claude가 관리 (읽기는 자유) |
| `website/index.html` | 아카이브 웹페이지 (더블클릭으로 열기) | ✗ 자동 생성 |
| `website/template.html` | 웹페이지 디자인 | 디자인 바꿀 때만 |
| `data/papers.json`, `data/topics.json` | 웹페이지용 데이터 | ✗ 자동 생성 |
| `logs/` | 실행 기록 | ✗ |

위키 안의 구성:
- `overview.md` — 목차 (주제 목록, 논문 수, 질의 기록)
- `log.md` — 변경 이력 (최신순)
- `papers/` — 논문 한 편당 한 페이지 (맨 위 속성에 연구 유형·종·영상 기법 등)
- `topics/` — 주제별 종합 (근거 표기, 상충되는 근거, 남은 질문)
- `queries/` — 저장된 질의응답
- `lint-report.md` — 최근 점검 보고서

---

## 할 수 있는 일 네 가지

터미널에서 먼저 프로젝트 폴더로 이동하세요.
```
cd /Users/kka/Documents/vet_paper_wiki
```

### 1) 수집 — 매주 자동 (수동 실행도 가능)
매주 월요일 오전 9시 cron이 `run_weekly.sh`를 실행합니다. 지금 바로 돌리고 싶으면:
```
./run_weekly.sh
```
새 논문을 가져와 선별 → 위키에 통합 → 웹페이지 갱신 → GitHub 반영까지 진행하고,
끝나면 맥 알림이 뜹니다. 중간에 멈춰도 처리 못 한 논문은 다음 실행 때 다시 처리됩니다.
매월 첫 주 실행에는 위키 점검(아래 4번)도 자동으로 포함됩니다.

### 2) 질문하기
```
./ask.sh "개 IVDD 평가에서 MRI와 CT를 비교한 근거 정리해줘"
```
위키에 쌓인 논문을 근거로 답하고, 다시 볼 가치가 있는 답은 `queries/`에 저장됩니다.
여러 번 대화하듯 묻고 싶으면 이 폴더에서 그냥 `claude`를 실행하면 됩니다.

### 3) 중요한 논문은 전문(PDF)으로 격상
`raw/pdf/` 폴더에 PDF를 넣어두세요 (파일 이름에 PMID를 넣으면 가장 정확합니다.
예: `42644764.pdf`). 다음 주간 실행 때 초록 기반 요약이 전문 기반으로 보강되고,
웹페이지에 "전문 검토" 배지가 붙습니다. PDF는 GitHub에 올라가지 않습니다.

### 4) 위키 점검 (평소엔 매월 자동)
```
./run_lint.sh
```
끊어진 링크, 연결 안 된 페이지, 합칠 만한 주제 등을 점검해 고치고
`obsidian_notes/lint-report.md`에 보고서를 남깁니다.

---

## 검색 조건 조정

`config.py`를 고친 뒤, 저장 없이 검색 결과 수만 먼저 확인해보세요.
```
python3 fetch_papers.py --dry-run
```
- 너무 많으면: `IMAGING_TERMS`에서 넓은 용어(예: `ultrasound[tiab]`)를 빼거나 `VET_CONTEXT_TERMS`를 줄이기
- 너무 적으면: 용어 추가, `DAYS_BACK` 늘리기
- 한 번에 처리할 최대 편수: `MAX_RESULTS` (넘친 논문은 다음 주로 이월)

주제 체계나 태그 목록을 바꾸고 싶으면 `CLAUDE.md`의 해당 표를 고치면 됩니다.

---

## 웹페이지 보기

- 내 컴퓨터: `website/index.html` 더블클릭 (바탕화면 가상본·Safari 즐겨찾기 가능)
- 밖에서: GitHub Pages 주소 `https://proj-x7k2.github.io/proj-x7k2/website/`
  (검색엔진 색인은 막혀 있지만, 주소를 아는 사람은 볼 수 있습니다)
- "논문" 탭: 검색·태그 필터, 연구 유형과 표본 수 배지
- "주제" 탭: 주제별 종합, 상충되는 근거, 남은 질문

---

## 자동 실행 설정 (이미 완료된 상태, 참고용)

- cron: `crontab -l` → `0 9 * * 1 /bin/bash /Users/kka/Documents/vet_paper_wiki/run_weekly.sh`
- 자동 깨우기: `pmset -g sched`로 월요일 오전 깨우기 확인 (전원 어댑터 연결 필요)
- 권한: 시스템 설정 → 개인정보 보호 및 보안 → 전체 디스크 접근 권한에 `/usr/sbin/cron` 켜짐
- 인증: `claude_token.txt` (구독 계정 토큰). 만료·오류 시 `claude setup-token`으로 재발급 후
  `echo -n "토큰" > claude_token.txt`
- 이 폴더에서 패키지 설치는 `python3 -m pip install -r requirements.txt`

---

## 문제 해결

| 증상 | 확인할 것 |
|---|---|
| 월요일에 로그 파일이 안 생김 | cron 권한(전체 디스크 접근), 맥 전원·깨우기 |
| 알림 "claude 명령을 찾을 수 없음" | 터미널에서 `which claude` 결과를 알려주세요 |
| 알림 "실행 중 오류 발생" | `logs/` 최신 파일의 마지막 부분 확인 |
| 논문이 너무 적거나 많음 | `python3 fetch_papers.py --dry-run` 후 `config.py` 조정 |
| 웹페이지가 옛날 내용 | `python3 build_site.py` 실행 |
| 위키 구조가 이상해짐 | `git log`로 이전 커밋 확인 후 되돌리기 가능 |
