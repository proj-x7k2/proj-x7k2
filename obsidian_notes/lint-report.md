# 점검 보고서 — 2026-11-02

## 점검 범위
논문 페이지 101편, 주제 페이지 16편(nuclear-medicine-imaging 포함), digests 2편, overview.md, log.md.
(Python 스크립트 실행이 승인되지 않아 Grep/grep 집계와 개별 열람으로 점검함.)

## 바로 고친 것
- `topics/sedation-restraint-imaging.md`: "현재까지의 종합" 첫 문장에 근거 표기가 없어 Liu 2026 링크와 (후향적 연구, n=93)을 추가함.
- 같은 파일 "남은 질문" 목록 중간의 빈 줄 제거(목록이 둘로 갈라져 있었음).

## 점검 결과 — 이상 없음
- **링크**: 논문·주제·digests·overview·log에서 참조된 `[[papers/...]]` 대상이 정확히 101개이며 모두 실제 파일과 일치(끊어진 링크 없음). `[[queries/...]]` 참조 없음.
- **양방향 연결**: 주제별 frontmatter `topics` 집계와 주제 페이지 "관련 논문" 항목 수가 16개 주제 모두 일치(합계 117건). 각 논문 파일에 `관련 주제:` 줄이 있음. 신규 17편은 개별 열람해 `topics` ↔ 주제 페이지 링크 확인.
- **overview.md**: 16개 주제 모두 있고 논문 수가 실제와 일치(abdominal 9, musculoskeletal 15, cardiac 18, neuro 14, technique 7, AI 7, trauma 5, spinal 8, urogenital 7, sedation 4, thoracic 3, vascular 4, head-neck 6, oncologic 4, nuclear 3, endocrine 3).
- **메타데이터**: 101편 모두 `starred`, `evidence_basis`, `added_on` 형식 정상. study_type·species·modality·system 값 전부 통제 어휘 안. 신규 17편은 `tags` = species+modality+system 합집합 확인(기존 84편은 10-07 점검 이후 변경 없음).
- **log.md**: 최신순 유지. (`data/skipped.json` 형식 검증은 스크립트 승인 문제로 하지 못함.)
- **상충되는 근거**: 이번 수집분에서 기존 결론과 충돌하는 내용은 찾지 못함.

## 한계
주제 페이지 16편 중 nuclear-medicine, oncologic, sedation-restraint는 전문을 읽었고, 나머지는 근거 표기가 없는 줄을 패턴 검색으로 훑었음. 문장 단위의 의미 점검(미표시 상충 등)은 전수하지 못함.

## 판단이 필요해 제안으로 남기는 것 (직접 바꾸지 않음)
1. **`2026-42876319-64cucl2-pet-ct-feline-mammary-carcinoma`를 `nuclear-medicine-imaging`에도 연결할지.** 이 논문은 modality에 `nuclear-medicine`이 있으나 `topics`는 `oncologic-imaging` 하나뿐이고, 핵의학 주제 페이지는 "oncologic-imaging 참고"로만 언급함. 2번째 주제로 추가하면 핵의학 주제가 3→4편이 되고 64CuCl2 근거가 한곳에서 보임.
2. **`2026-42150942-ai-assisted-radiograph-interpretation`의 `species: []`.** 종 특정이 없는 종설이라 빈 값 자체는 허용되지만 웹사이트 종 필터에서 빠질 수 있음. 초록을 확인해 `dog`/`cat`을 넣을지 결정 필요.
3. **논문 3~4편 주제**(thoracic, endocrine, nuclear-medicine 각 3편; vascular, sedation-restraint, oncologic 각 4편)는 모두 CLAUDE.md 표의 공식 주제이고 범위가 겹치지 않아 병합하지 않음. 다음 점검까지 추이만 관찰 권장.
4. **"(아직 없음)" 자리표시자.** musculoskeletal, abdominal, neuro 3개 주제의 "## 상충되는 근거"에 "(아직 없음)"이 적혀 있음. 스키마는 "있을 때만"이라 제목째 지워도 되지만, 의도된 표기일 수 있어 그대로 둠.
5. **DOI 공란 논문.** 수집 로그상 PubMed 원자료의 DOI가 논문과 맞지 않아 `doi: ""`로 둔 논문이 다수임. raw/는 수정 불가이므로 필요하면 사용자가 원문에서 확인해 채워야 함.
