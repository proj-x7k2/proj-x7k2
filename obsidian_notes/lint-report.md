# 점검 보고서 — 2026-10-07

## 점검 범위
논문 페이지 62편, 주제 페이지 15편(endocrine-imaging 포함) 전체를 대상으로 다음을 확인:
- 논문 ↔ 주제 양방향 링크(frontmatter `topics`, 본문 "관련 주제", 주제 페이지 "관련 논문")
- 끊어진 `[[...]]` 링크
- 메타데이터 통제 어휘(species/modality/system/study_type) 준수, `tags` = species+modality+system 합집합 여부
- overview.md 주제 목록·논문 수가 실제와 일치하는지
- 주제 종합 문단의 근거 표기(논문 링크 + 연구유형·n) 누락 여부, 상충 근거 미표시 여부
- 논문 1~2편 주제의 병합 적합성

## 바로 고친 것
- **overview.md에 `endocrine-imaging` 주제 항목이 빠져 있었음.** `topics/endocrine-imaging.md`와 논문 `papers/2026-42815534-ct-perfusion-pheochromocytoma.md`는 정상적으로 서로 링크되어 있었으나, 지난 수집 때 overview.md 목록 갱신에서만 누락됨. "주요 주제" 목록 끝에 `- [[topics/endocrine-imaging]] — 부신, 갑상선, 부갑상선, 뇌하수체 영상 (논문 1편)` 한 줄을 추가함.

## 점검 결과 — 이상 없음
- **링크 정합성**: 논문 62편 전원이 frontmatter `topics`에 적힌 모든 주제 페이지로부터 역링크를 받고 있고, 주제 페이지 15편 각각의 "관련 논문" 목록이 그 주제를 참조하는 논문 집합과 정확히 일치함(논문-주제 연결 73건 전수 대조, 끊어진 링크·한쪽만 걸린 링크 0건).
- **메타데이터**: species/modality/system/study_type 값 전부가 CLAUDE.md 통제 어휘 목록 안에 있고, `tags`는 모든 논문에서 species+modality+system의 합집합과 정확히 일치함. `sample_size`가 빈 문자열인 경우(예: `42746025`, `42797990`)는 초록에 표본 수가 명시되지 않은 경우로, 스키마상 허용된 처리임.
- **주제 종합 문단**: 15개 주제 페이지 전체를 읽고 "관련 논문" 목록과 본문 인용을 대조한 결과, 핵심 주장마다 논문 링크와 (연구유형, n)이 달려 있었고 근거 표기가 빠진 문장은 발견되지 않음. 명백히 상충되는데 "## 상충되는 근거"에 표시되지 않은 내용도 없었음.
- **raw/, data/papers.json, data/topics.json, website/**: 이번 점검에서 열람만 하고 수정하지 않음.

## 판단이 필요해 제안으로 남기는 것 (직접 병합하지 않음)
- `endocrine-imaging`(논문 1편)과 `oncologic-imaging`(논문 1편)은 논문 수가 가장 적은 주제이지만, 둘 다 CLAUDE.md 주제 체계 표에 원래부터 있던 계통 교차형 주제(내분비, 종양 영상 원칙)로 다른 주제의 소제목으로 흡수하기엔 범위가 뚜렷이 다름(부신/갑상선/뇌하수체, 병기·전이 평가는 특정 장기계통 주제와 겹치지 않음). 지금 병합하기보다 다음 1~2회 수집에서 논문이 더 들어오는지 지켜보는 것을 권장함.
- `sedation-restraint-imaging`, `thoracic-imaging`, `vascular-imaging`, `head-neck-imaging`(각 2편)도 논문 수가 적지만 모두 CLAUDE.md 표의 공식 주제이고 서로 범위가 겹치지 않아, 병합 대상으로 보지 않음.

## 요약
- 고친 것: overview.md 주제 목록에 `endocrine-imaging` 1줄 추가.
- 제안: 없음(구조 변경 필요 사항 미발견). 논문 1편뿐인 `endocrine-imaging`·`oncologic-imaging`은 당장 병합하지 말고 추이만 지켜보자는 관찰 메모만 남김.
