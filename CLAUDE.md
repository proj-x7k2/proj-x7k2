# 수의영상의학 논문 LLM 위키 — 관리 스키마 (v2)

이 폴더는 PubMed에서 자동 수집한 소동물 영상의학 논문을 바탕으로 **누적되는 위키**를
유지합니다. 새 논문은 단순히 카드로 쌓이지 않고, 정해진 주제 체계 안의 주제 페이지에
통합되어 종합 결론을 계속 다듬습니다. 당신(Claude)은 위키의 관리자이고, 사용자는
자료 선택·질문·방향 결정을 맡습니다.

## 독자

- 개·고양이 위주, 드물게 토끼를 보는 2차 동물병원 임상수의사 (영상의학 중심, 심장·신경·외과·종양 증례 병행)
- 1.5T MRI, CT, 초음파를 실제로 운용함 → 임상 시사점은 "내일 진료/촬영에서 무엇을 다르게 할지" 수준으로 구체적으로
- 영어 논문을 읽는 데 익숙하므로 전문 용어는 영어 원어 유지 (아래 스타일 원칙)

## 레이어와 폴더

```
raw/                         원자료 층 — 읽기만, 절대 수정·삭제 금지
  pubmed/{pmid}.json         PubMed 원자료 (초록, publication_types, MeSH 포함)
  pdf/                       사용자가 넣는 논문 전문 PDF (있으면 전문 기반으로 격상)
data/
  raw_papers.json            이번 실행에서 처리할 논문 목록 (스크립트가 만듦)
  skipped.json               의도적으로 건너뛴 논문 기록 (당신이 추가)
  papers.json, topics.json   웹사이트용 — 스크립트가 자동 생성. 직접 수정 금지
obsidian_notes/              위키 층 — 당신이 전적으로 관리
  overview.md                목차(index): 주제 목록과 논문 수, 질의 기록
  log.md                     변경 기록: 수집·질의·점검 이력을 최신순으로
  papers/{year}-{pmid}-{short-slug}.md    논문 페이지
  topics/{topic-slug}.md     주제 종합 페이지
  queries/{date}-{slug}.md   가치 있는 질의응답 결과
  lint-report.md             가장 최근 점검 보고서
CLAUDE.md                    이 문서 (스키마)
```

`website/index.html`, `data/papers.json`, `data/topics.json`은 절대 직접 고치지 마세요.
위키 페이지만 고치면 스크립트(`build_site.py`)가 자동으로 반영합니다.

## 통제 어휘 (메타데이터와 태그에는 이 목록의 값만 사용)

- species: `dog`, `cat`, `rabbit`
- modality: `radiography`, `CT`, `MRI`, `ultrasound`, `echocardiography`, `fluoroscopy`,
  `nuclear-medicine`, `contrast-study`, `interventional`
- system: `neuro`, `spine`, `head-neck`, `dental`, `thorax`, `cardiovascular`, `abdomen`,
  `hepatobiliary`, `gastrointestinal`, `urogenital`, `endocrine`, `musculoskeletal`,
  `oncology`, `trauma`, `technique`, `sedation-restraint`, `AI`
- study_type: `증례보고`, `증례군`, `후향적 연구`, `전향적 연구`, `무작위대조군연구`,
  `실험 연구`, `종설`, `메타분석`, `기타`
  (PubMed의 publication_types를 참고하되, 최종 판단은 초록의 방법론 서술로)

목록에 없는 값이 꼭 필요하면 이 문서의 목록에 먼저 추가하고, log.md에 사유를 남기세요.

## 주제 체계

주제는 아래 목록에서 고르는 것이 원칙입니다. 파일은 첫 논문이 들어올 때 만듭니다.
세부 주제(예: "토끼 CT 보정법", "CT 선량 추정")는 새 페이지가 아니라 해당 주제 페이지
안의 `###` 소제목으로 넣으세요.

| slug | 이름 | 범위 |
|---|---|---|
| neuro-imaging | 뇌·두개내 영상 | 뇌, 뇌신경, 두개내 병변 |
| spinal-imaging | 척추·척수 영상 | IVDD, 척수병증, 척추 기형 |
| head-neck-imaging | 두경부 영상 | 비강, 중이, 안와, 후두, 침샘, 치아·턱 |
| thoracic-imaging | 흉부 영상 | 폐, 기도, 종격, 흉막 |
| cardiac-imaging | 심장·대혈관 영상 | 심초음파, 심장 CT, 대혈관 |
| abdominal-imaging | 복부·소화기 영상 | 위장관, 간담도, 췌장, 비장, 복강 |
| urogenital-imaging | 비뇨생식기 영상 | 신장, 요관, 방광, 전립선, 생식기 |
| endocrine-imaging | 내분비 영상 | 부신, 갑상선, 부갑상선, 뇌하수체 |
| musculoskeletal-imaging | 근골격 영상 | 관절, 골, 근육, 골종양 |
| vascular-imaging | 혈관 영상·중재 | 문맥전신단락, 혈관 기형, 중재 시술 |
| oncologic-imaging | 종양 영상 원칙 | 병기 결정, 전이 평가 등 계통을 넘는 종양 영상 |
| trauma-forensic-imaging | 외상·법수의학 영상 | 다발성 외상, 학대 의심 평가 |
| imaging-technique-safety | 촬영 기법·안전 | 프로토콜, 조영제, 방사선 선량, 영상 품질 |
| sedation-restraint-imaging | 영상검사 진정·보정 | 진정·마취·물리적 보정 |
| ai-imaging | AI·정량 영상 | AI 판독, 정량 분석, 영상 기반 모델 |

- 한 논문은 가장 적합한 주제 1개(필요하면 최대 2개)에 연결합니다.
- 목록의 어느 주제에도 맞지 않고 앞으로도 논문이 계속 나올 영역일 때만 새 주제를
  만들고, 이 표에 행을 추가한 뒤 log.md에 사유를 남기세요.

## 워크플로우 A — 수집 (매주 자동 실행)

1. `data/raw_papers.json`을 읽습니다. 빈 배열이면 "새 논문 없음"만 출력하고 끝냅니다.
2. 작업 전에 `obsidian_notes/overview.md`를 읽어 현재 주제 목록을 파악하고, 필요하면
   Glob/Grep으로 기존 페이지를 찾습니다 (예: 같은 pmid의 페이지가 이미 있는지).
3. **선별(triage)** — 다음에 해당하면 위키에 넣지 말고 `data/skipped.json` 배열에
   `{"pmid": "...", "title": "...", "reason": "...", "date": "YYYY-MM-DD"}`를 추가합니다.
   - 영상이 부수적인 경우 (예: 항암 임상시험에서 CT를 병기 결정에만 사용)
   - 사람 질환 연구를 위한 실험동물 모델 연구
   - 대상 종이 개·고양이·토끼가 아닌 경우 (여러 종 중 하나로 포함되면 통과 가능)
   애매하면 넣는 쪽을 택하세요.
4. **통과한 논문마다**:
   a. `raw/pubmed/{pmid}.json`이 있으면 그것을 원자료로 사용합니다.
   b. 논문 페이지를 아래 형식으로 만듭니다. 파일명은 `{year}-{pmid}-{short-slug}.md`
      (short-slug는 제목 핵심어 3~5개, 소문자·하이픈).
   c. 주제 체계에서 주제를 고르고, 해당 주제 페이지를 **반드시 먼저 읽은 뒤** 새 근거를
      통합합니다. 기존 문장은 살리고 새 근거를 자연스럽게 덧붙이세요. 통째로 다시 쓰지 마세요.
   d. 새 근거가 기존 결론과 다르면 조용히 바꾸지 말고 "## 상충되는 근거"에 양쪽을 명시합니다.
   e. 이 논문으로 새로 드러난 근거 공백이 있으면 "## 남은 질문"에 추가합니다.
   f. 논문 페이지 ↔ 주제 페이지 링크를 서로 겁니다.
5. `obsidian_notes/overview.md`의 주제 목록(논문 수 포함)을 갱신합니다.
6. `obsidian_notes/log.md` 맨 위에 기록을 추가합니다:
   `## YYYY-MM-DD 수집` 아래에 처리 N편, 건너뜀 M편(사유 요약), 신설·갱신된 주제.
7. 마지막에 처리/건너뜀 편수와 갱신된 주제를 한두 줄로 출력합니다.

## 워크플로우 B — 전문(PDF) 반영

`raw/pdf/`에 PDF가 있고, 대응하는 논문 페이지의 `evidence_basis`가 `abstract`이면
(파일명에 pmid가 있거나, 첫 페이지 제목으로 매칭):
- 논문 페이지에 "## 전문 검토" 섹션을 추가합니다: 연구 대상과 방법 상세, 핵심 수치
  (민감도·특이도, 측정값, 신뢰구간 등), 저자가 밝힌 한계와 당신이 보는 한계.
- 필요하면 국문 요약과 임상 시사점을 전문 기준으로 다듬고, `evidence_basis: "fulltext"`로 바꿉니다.
- 관련 주제 페이지의 해당 문장도 전문 기준으로 보강하고 log.md에 기록합니다.
수집 실행 때마다 이 확인을 함께 수행하세요.

## 워크플로우 C — 질의 (사용자가 이 폴더에서 질문할 때)

1. overview.md → 관련 주제 페이지 → 논문 페이지 순서로 읽고, 필요하면 raw/ 원자료까지 확인합니다.
2. 답에는 근거 논문을 `[[papers/...]]` 링크와 (연구 유형, n)으로 표시하고,
   위키 근거에서 나온 내용과 당신의 일반 지식을 구분해서 말합니다.
   근거가 초록만 기반이면 그 사실도 밝힙니다.
3. 여러 논문을 종합한 답처럼 다시 볼 가치가 있으면 `queries/{YYYY-MM-DD}-{slug}.md`로
   저장하고 (형식 아래), overview.md의 "질의 기록"과 log.md에 추가합니다.
4. 질의 중 주제 페이지에 반영할 통찰(새 연결, 공백, 모순)이 드러나면 해당 주제 페이지도 갱신합니다.

## 워크플로우 D — 점검 (매월 첫 주 자동 실행)

다음을 점검합니다.
- 끊어진 링크, 어느 주제에도 연결되지 않은 논문 페이지, 링크가 한쪽만 걸린 경우
- 메타데이터 누락·형식 오류, 통제 어휘 밖의 값
- overview.md의 주제 목록·논문 수가 실제와 맞는지
- 논문 1~2편뿐인 주제 중 다른 주제의 소제목으로 합치는 게 나은 것
- 주제 종합 문단이 관련 논문 목록과 어긋나거나, 근거 표기가 빠진 문장
- 상충되는 근거로 표시할 만한데 표시되지 않은 내용

기계적인 문제(링크, 메타데이터, 목록, 태그)는 바로 고칩니다. 주제 병합은 명백한 경우에만
직접 하고, 판단이 필요한 것은 보고서에 제안으로 남깁니다. 결과를
`obsidian_notes/lint-report.md`에 (덮어써서) 저장하고 log.md에 `## YYYY-MM-DD 점검` 기록을 남깁니다.

## 논문 페이지 형식

메타데이터 값은 반드시 JSON 형식(문자열은 큰따옴표, 목록은 대괄호)으로 쓰세요.
날짜만 따옴표 없이 씁니다.

```markdown
---
pmid: "42644764"
title: "Bunny Burrito Restraint for Computed Tomography in Conscious Rabbits: An Effective Alternative."
journal: "Veterinary Radiology & Ultrasound"
year: "2026"
authors: ["Hung-Ting Liu", "Jonathan Olijnyk"]
doi: "10.1111/vru.70230"
url: "https://pubmed.ncbi.nlm.nih.gov/42644764/"
study_type: "후향적 연구"
sample_size: "93"
species: ["rabbit"]
modality: ["CT"]
system: ["sedation-restraint", "dental"]
topics: ["sedation-restraint-imaging"]
tags: ["rabbit", "CT", "sedation-restraint", "dental"]
evidence_basis: "abstract"
added_on: 2026-09-13
---
# {제목}

**{저널} ({연도})** · {연구 유형}, n={표본 수} · [PubMed]({url}) · DOI: {doi}
관련 주제: [[topics/{topic-slug}]]

## 국문 요약
{3-4문장}

## English summary
{3-4 sentences}

## 임상 시사점
{1-2문장, 국문. 실제 진료·촬영에서 달라질 점}

## 연구 설계와 한계
{대상·설계·비교군·주요 한계를 2-3문장으로. 초록에 없는 정보는 추측하지 말 것}

## 원문 초록
{abstract}
```

- `tags`는 species + modality + system의 합집합입니다 (Obsidian 태그 창과 웹사이트 필터용).
- `sample_size`를 초록에서 알 수 없으면 `""`로 둡니다.

## 주제 페이지 형식

```markdown
---
title: "영상검사 진정·보정"
scope: "진정·마취·물리적 보정"
updated: 2026-09-21
---
# 영상검사 진정·보정

## 현재까지의 종합
{주제 전체의 현재 결론. 필요하면 ### 소제목으로 세부 주제를 나눔}

### 토끼 CT의 물리적 보정
{문장마다 근거 표기: "…움직임 인공물이 적었다 ([[papers/2026-42644764-bunny-burrito-restraint|Liu 2026]]; 후향적, n=93)."}

## 상충되는 근거
{있을 때만}

## 남은 질문
{근거가 아직 없거나 약한, 임상적으로 중요한 질문}

## 관련 논문
- [[papers/2026-42644764-bunny-burrito-restraint]] — 한 줄 핵심 (후향적, n=93)
```

## 질의 페이지 형식

```markdown
---
question: "{질문}"
date: 2026-09-21
papers: ["42644764", "42531994"]
---
# {질문}

{답변 — 근거 표기 포함, 위키 근거와 일반 지식 구분}
```

## overview.md 형식

```markdown
# 수의영상의학 논문 위키 개관

## 주요 주제
- [[topics/{slug}]] — {한 줄 설명} (논문 N편)

## 질의 기록
- [[queries/{파일명}]] — {질문 요약}
```
(변경 이력은 overview.md가 아니라 log.md에 남깁니다.)

## 스타일 원칙

- 서술은 국문, **의학·해부학·영상의학 전문 용어(질환명, 해부학적 구조, 영상 기법,
  시퀀스, 약물명 등)는 번역하지 않고 영어 원어를 그대로** 씁니다.
  - 권장: "이 종양은 T2-weighted 영상에서 hyperintense 신호를 보였다."
  - 지양: "이 종양은 T2 강조 영상에서 고신호강도를 보였다."
- 주제 종합의 모든 핵심 주장에는 근거 논문과 (연구 유형, n)을 붙입니다.
  증례보고·소규모 후향적 연구만으로 뒷받침되는 결론은 "제한적 근거"라고 명시합니다.
- 초록에 없는 수치나 결론을 만들어내지 마세요. 모르면 모른다고 씁니다.
- 주제 종합은 기존 문장을 살리며 갱신하고, 히스토리를 존중하는 편집을 합니다.
