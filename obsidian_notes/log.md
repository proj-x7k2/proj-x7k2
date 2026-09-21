# 변경 기록

## 2026-09-21 v2 전환
- 위키 전체를 v1 형식에서 CLAUDE.md v2 스키마로 전환. 기존 요약 내용은 보존하고 형식·구조만 변경.
- 논문 페이지 5편 전체를 `{year}-{pmid}-{short-slug}.md` 파일명으로 재생성하고, `raw/pubmed/{pmid}.json`을 참고해 메타데이터(species, modality, system, study_type, sample_size 등 통제 어휘)를 채움. 본문 속 `#태그` 줄 삭제, "연구 설계와 한계" 섹션 신설.
  - `2026-42522404-ssde-canine-abdominal-ct` (SSDE 개 abdominal CT 선량 추정): `raw/pubmed/42522404.json`에 원문 초록 전체가 확보되어 있어, 기존에 "초록이 잘렸다"고 기록했던 국문/영문 요약과 임상 시사점을 전체 초록 기준 수치(R²=0.94, CTDIvol 50% 과소평가, SSDE 75th percentile 21 mGy 등)로 보강함.
- 주제 페이지를 v2 주제 체계로 재편 및 근거 표기(저자·연도, 연구 유형, n) 추가:
  - `ai-veterinary-imaging` → `ai-imaging`
  - `ct-dose-estimation` → `imaging-technique-safety` (### CT 방사선 선량 추정 소제목)
  - `conscious-imaging-restraint` → `sedation-restraint-imaging` (### 토끼 CT의 물리적 보정 소제목)
  - `forensic-imaging` → `trauma-forensic-imaging`
  - 각 주제 페이지에 "남은 질문" 섹션 신설.
- `overview.md`를 v2 형식(주요 주제 + 논문 수, 질의 기록)으로 재작성. 과거 "최근 업데이트" 이력은 이 log.md로 이관.
- `data/papers.json`, `data/topics.json`, `website/`, `raw/`는 변경하지 않음 (빌드 스크립트가 자동 생성).

## 2026-09-13 수집
- 논문 4편 처리. 신규 주제 3개 생성 — 의식 하 영상검사 보정 기법(토끼 CT 번니 부리토), CT 방사선 선량 추정(개 복부 CT SSDE), 수의영상의학 AI 활용(서지계량 분석 + 임상 모범사례, 2편 통합).

## 2026-09-13 점검
- 순수 영상의학 주제가 아닌 topic(자궁축농증 수술 예후, 항생제 내성, 방광 이행상피암 스크리닝, 면역관문억제제 항암치료, 전기화학요법)과 관련 논문 페이지, `data/papers.json` 항목을 정리. 법수의학 영상진단(forensic-imaging)만 유지.

## 2026-09-13 수집
- 논문 7편 처리. 신규 주제 6개 생성 — 법수의학 영상진단, 자궁축농증 수술 예후, 항생제 내성, 방광 이행상피암 스크리닝, 면역관문억제제 항암치료, 전기화학요법(2편 통합).
