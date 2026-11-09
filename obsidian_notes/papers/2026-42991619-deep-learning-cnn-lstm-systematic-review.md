---
pmid: "42991619"
title: "Deep learning for diagnostic and clinical decision support in companion animals: a systematic review of CNN- and LSTM-based approaches."
journal: "Frontiers in Veterinary Science"
year: "2026"
authors: ["Juan J Guevara-Flores", "Jhonatan López-Rojas", "José A Vásquez-Coronel"]
doi: ""
url: "https://pubmed.ncbi.nlm.nih.gov/42991619/"
study_type: "종설"
sample_size: "57"
species: ["dog", "cat"]
modality: ["radiography", "ultrasound"]
system: ["AI"]
topics: ["ai-imaging"]
tags: ["dog", "cat", "radiography", "ultrasound", "AI"]
evidence_basis: "abstract"
added_on: 2026-11-09
starred: false
---
# Deep learning for diagnostic and clinical decision support in companion animals: a systematic review of CNN- and LSTM-based approaches.

**Frontiers in Veterinary Science (2026)** · 종설(systematic review, PRISMA 2020), n=57편 · [PubMed](https://pubmed.ncbi.nlm.nih.gov/42991619/)
관련 주제: [[topics/ai-imaging]]

## 국문 요약
Scopus와 Web of Science에서 2021-2026년 출판된 개·고양이 대상 CNN·LSTM 기반 진단/임상 의사결정 지원 연구 57편을 PRISMA 2020과 PICO-CS 틀로 체계적으로 검토했다. 근거는 oncology(28.1%), cardiology(15.8%), pulmonology(12.3%)에 집중되었다. CNN은 radiograph·임상 사진·초음파·현미경 영상 같은 공간적 영상에, LSTM은 시계열 신호와 센서 자료에 쓰였다. Binary classification은 accuracy 최대 99%까지 보고되었으나 multi-class는 데이터 불균형으로 변동이 컸고, 데이터셋·평가지표·검증 방식의 이질성이 크며 고성능 연산 인프라 의존이 현장 적용의 장벽으로 지목되었다.

## English summary
This PRISMA 2020 systematic review of 57 primary studies (2021-2026) examined CNN- and LSTM-based diagnostic support in dogs and cats. Evidence concentrated in oncology, cardiology and pulmonology. CNNs dominated imaging modalities (radiographs, photographs, ultrasonography, microscopy); LSTMs were used for temporal signals. Binary tasks reached up to 99% accuracy, whereas multi-class tasks varied widely, with substantial heterogeneity in datasets and validation. The authors call for prospective external validation, open representative datasets and lightweight models.

## 임상 시사점
논문에서 보고되는 "accuracy 99%"는 대부분 binary 과제의 내부 검증 값이므로, AI 판독 도구를 도입할 때는 외부 병원 자료에서의 prospective 검증 여부와 multi-class 성능을 먼저 확인해야 한다. 영상(영상의학) 외 연구도 섞여 있어 영상 판독 성능으로 그대로 해석하지 않는다.

## 연구 설계와 한계
두 데이터베이스만 검색했고 영상 연구와 비영상(LSTM, 센서) 연구가 함께 포함되어 영상의학만의 결론은 아니다. 초록에는 영상 modality별 성능 수치, 종별 분포, 편향 위험 평가 결과가 제시되지 않았다. 저자들이 지적한 이질성 때문에 연구 간 직접 비교(meta-analysis)는 이루어지지 않았다.

## 원문 초록
Early disease detection prior to the onset of advanced clinical signs remains a critical imperative in veterinary medicine. This systematic review provides a methodological synthesis of Convolutional Neural Networks and Long Short-Term Memory networks applied to diagnostic and clinical decision support in canine and feline patients, evaluating both algorithmic performance and clinical feasibility. Adhering to the PICO-CS framework and PRISMA 2020 guidelines, we queried Scopus and Web of Science for peer-reviewed studies published between 2021 and 2026, retrieving a final corpus of 57 primary studies. Eleven clinical domains were identified, with evidence heavily concentrated in Oncology (28.1%), Cardiology (15.8%), and Pulmonology (12.3%). CNN architectures predominated in spatial imaging modalities-including radiographs, clinical photography, ultrasonography, and microscopic imagery-whereas LSTM networks were deployed for temporal signals and sensor-derived telemetry. Binary classification tasks achieved the highest performance metrics (accuracy reaching up to 99%), whereas multi-class formulations exhibited broader variability due to dataset imbalance. Cross-study benchmarking revealed substantial heterogeneity in datasets, evaluation metrics, and validation protocols, while reliance on high-performance computational infrastructure poses a barrier to point-of-care deployment in resource-constrained clinics. We conclude that while deep learning architectures hold significant promise as clinical decision-support tools, transitioning to routine veterinary practice requires prospective external validation, representative open-access datasets, and lightweight models optimized for conventional clinical hardware.
