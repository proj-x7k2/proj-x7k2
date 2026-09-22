---
title: "AI·정량 영상"
scope: "AI 판독, 정량 분석, 영상 기반 모델"
updated: 2026-09-22
---
# AI·정량 영상

## 현재까지의 종합
수의영상의학 분야에서 AI, 특히 딥러닝 기반 자동 판독 기술에 대한 관심과 연구가 빠르게 증가하고 있다. 2018-2025년 소동물 흉부 radiography 관련 AI 문헌 27편을 분석한 서지계량 연구에 따르면, 연구 출판은 연평균 10.41%씩 증가해 2023년 정점(8편)을 찍었고, 미국과 이탈리아가 주요 연구 생산국이었으며, 개의 cardiomegaly·pleural effusion·pulmonary disease에 대한 CNN(convolutional neural network)·deep learning 기반 자동 탐지가 초기 연구의 핵심 주제였다 ([[papers/2026-42593822-ai-bibliometric-thoracic-radiography|Canatan 2026]]; 기타/서지계량분석, n=27편). 다만 데이터셋의 이질성과 대상 종·품종의 다양성 부족이 표준화의 걸림돌로 지목되었다([[papers/2026-42593822-ai-bibliometric-thoracic-radiography|Canatan 2026]]; 기타/서지계량분석, n=27편). 이 분석은 개별 AI 알고리즘의 진단 정확도가 아니라 문헌 동향 자체를 다룬 것이라는 점에 유의해야 한다.

임상 적용 측면에서는, AI는 어디까지나 clinical judgment를 보조하는 decision support tool로 자리매김해야 하며 최종 진단과 치료 결정에 대한 책임은 여전히 수의사에게 있다는 점이 강조된다 ([[papers/2026-42150942-ai-assisted-radiograph-interpretation|Basran 2026]]; 종설). 보호자에게 AI의 작동 방식과 한계를 이해하기 쉽게 설명할 수 없다면 임상에 도입해서는 안 되며, 성공적인 도입을 위해서는 팀 교육, 전통적 판독 능력 유지, quality assurance 체계가 필요하다([[papers/2026-42150942-ai-assisted-radiograph-interpretation|Basran 2026]]; 종설). 이 권고는 정량적 검증 연구가 아니라 임상의 관점의 종설에 기반한 것으로, 원저 수준의 근거는 아니다.

### 영상 기반 정량 예측 모델
판독 보조를 넘어, 영상에서 추출한 정량 데이터를 머신러닝으로 예측에 활용하는 연구도 등장하고 있다. Appendicular osteosarcoma를 가진 개 16마리의 CT 영상에서 재구성한 뼈 모델로 FEA(Finite Element Analysis)·XFEM 시뮬레이션을 수행하고, 이 시뮬레이션 데이터(825건)로 여러 머신러닝 모델(MLP, SVR, RF, XGBoost, HistGBR)을 학습시켜 골절 하중을 예측한 연구에서는 XGBoost가 held-out 165건에서 평균 R²≈0.90, 정규화 평균절대오차 약 8%의 성능을 보였다 ([[papers/2026-42705596-ml-fracture-load-prediction-osteosarcoma-ct|Amirzade 2026]]; 실험 연구, n=16). 병변 부담(lesion burden)과 체중이 가장 중요한 예측 인자였으나, 저자들 스스로 이것이 proof-of-concept 단계이며 실제 임상 결과(치료된 개 6마리)는 서술적 참고일 뿐 공식 검증이 아니라고 명시했다 — 제한적 근거. 같은 맥락에서 canine glioma의 T2-FLAIR MRI radiomics(texture, shape, intensity) 특징을 human glioblastoma와 비교한 연구는 선별된 radiomic feature가 종양·비병변 조직을 AUC 80% 이상으로 구별했고, 개·사람 통합 SVM 모델이 80.33%의 정확도를 보여 translational 모델로서의 가치를 시사했다 ([[papers/2026-42746025-radiomics-canine-glioma-mri|Faustino 2026]]; 후향적 연구, n="" — 상세는 [[topics/neuro-imaging]] 참고). 다만 이 연구도 canine 단독 증례 수·진단 성능이 별도로 제시되지 않아 임상 진단 도구로 쓰기는 이르다.

## 남은 질문
- 실제 임상에서 사용 가능한 개별 AI 판독 도구의 민감도·특이도를 종·품종별로 검증한 원저 연구는 이 위키에 아직 없다.
- AI 보조진단 도구의 quality assurance 체계를 실제 2차 동물병원 워크플로우에 어떻게 통합할지에 대한 구체적 지침은 부족하다.
- CT-FEA-ML 기반 골절 하중 예측, radiomics 기반 종양 판별 모두 proof-of-concept 단계로, 전향적·다기관 임상 검증이 아직 없다.

## 관련 논문
- [[papers/2026-42593822-ai-bibliometric-thoracic-radiography]] — 2018-2025년 소동물 흉부 radiography AI 문헌 27편 서지계량 분석, CNN 기반 자동탐지가 주요 초점 (기타/서지계량분석, n=27편)
- [[papers/2026-42150942-ai-assisted-radiograph-interpretation]] — AI는 의사결정 보조도구이며 최종 책임은 수의사에게 있다는 임상 관점의 모범사례 (종설)
- [[papers/2026-42705596-ml-fracture-load-prediction-osteosarcoma-ct]] — CT-FEA-ML로 osteosarcoma 골절 하중 예측, proof-of-concept (실험 연구, n=16)
- [[papers/2026-42746025-radiomics-canine-glioma-mri]] — T2-FLAIR radiomics로 canine glioma·human glioblastoma 종양 조직 판별 (후향적 연구, n="")
