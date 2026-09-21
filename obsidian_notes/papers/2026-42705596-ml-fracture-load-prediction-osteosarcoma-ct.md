---
pmid: "42705596"
title: "Mechanistic-data synergy for predicting fracture load in canine bone with appendicular osteosarcoma."
journal: "Veterinary journal (London, England : 1997)"
year: "2026"
authors: ["Behzad Amirzade", "Tareq Zobaer", "Janis Lapsley", "Kim A Selting", "Laura E Selmic", "Ali Nassiri"]
doi: "10.1016/j.tvjl.2026.106873"
url: "https://pubmed.ncbi.nlm.nih.gov/42705596/"
study_type: "실험 연구"
sample_size: "16"
species: ["dog"]
modality: ["CT"]
system: ["musculoskeletal", "oncology", "AI"]
topics: ["musculoskeletal-imaging", "ai-imaging"]
tags: ["dog", "CT", "musculoskeletal", "oncology", "AI"]
evidence_basis: "abstract"
added_on: 2026-09-21
---
# Mechanistic-data synergy for predicting fracture load in canine bone with appendicular osteosarcoma.

**Veterinary journal (London, England : 1997) (2026)** · 실험 연구, n=16 (CT 기반 뼈 모델; ML 평가는 165건 held-out) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/42705596/) · DOI: 10.1016/j.tvjl.2026.106873
관련 주제: [[topics/musculoskeletal-imaging]] · [[topics/ai-imaging]]

## 국문 요약
Appendicular osteosarcoma를 가진 개 16마리의 CT 영상에서 재구성한 이질적(heterogeneous) elasto-plastic 물성치를 가진 물리 기반 뼈 모델을 이용해, 고신뢰도 Finite Element Analysis(FEA)·XFEM 시뮬레이션(25가지 하중 조건, medullary conformal stabilization 유무)으로 825개의 crack-initiation load 데이터를 생성했다. 이 시뮬레이션 데이터로 MLP, SVR, RF, XGBoost, HistGBR 등 5가지 머신러닝 모델을 학습시켜 체중, 병변 위치, 뼈 길이 등과 골절 하중의 관계를 예측하도록 했으며, XGBoost가 held-out 165건에서 평균 R²≈0.90, 정규화 평균절대오차 약 8%로 가장 우수했다. 병변 부담(lesion burden)과 체중이 가장 중요한 예측 인자였고, humerus 증례에서 tibia·radius보다 환자 단위 예측 성능이 더 일관됐다.

## English summary
Using CT-derived, physics-faithful bone models with heterogeneous elasto-plastic material properties from 16 dogs with appendicular osteosarcoma, this study generated 825 crack-initiation load values via high-fidelity Finite Element Analysis (FEA) and XFEM simulations across 25 loading scenarios, with and without medullary conformal stabilization. Five machine learning models (MLP, SVR, RF, XGBoost, HistGBR) were trained on these simulation-derived targets plus biological/morphometric features; XGBoost achieved the best performance on 165 held-out cases (average R²≈0.90, ~8% normalized mean absolute error). Lesion burden and body weight were the dominant predictors, with more consistent patient-level performance for humeral than tibial/radial cases.

## 임상 시사점
현재는 개념 증명(proof-of-concept) 단계이지만, CT 영상에서 추출한 뼈 형상·물성 데이터를 이용한 ML 골절 하중 예측이 향후 osteosarcoma 환자의 예방적 내고정 필요성 판단을 보조하는 정량 도구로 발전할 가능성이 있다 — 제한적 근거.

## 연구 설계와 한계
CT 스캔 16마리의 뼈 모델을 이용한 FEA/XFEM 시뮬레이션과 이를 학습 데이터로 한 ML 대리모델(surrogate model) 개발 연구로, 실제 임상 결과(치료된 개 6마리)는 기술적(descriptive) 맥락으로만 제시되었을 뿐 공식적인 검증(validation)은 아니라고 저자들이 명시했다. Humerus 대비 tibia·radius 증례에서 환자 단위 일반화 성능이 낮았고, 더 크고 뼈 종류가 균형 잡힌 데이터셋이 필요하다고 밝혔다.

## 원문 초록
Canine appendicular osteosarcoma substantially increases the risk of pathological fractures. Limb-sparing approaches such as Stereotactic Body Radiation Therapy (SBRT) can extend and improve the quality of life in large-breed dogs; however, recent clinical studies have reported high post-SBRT fracture rates and significant complications following prophylactic stabilization. While patient-specific Finite Element Analysis (FEA) can estimate pre- and post-stabilization fracture-initiation thresholds, its computational burden limits its clinical applicability. This study presents Machine Learning (ML) surrogates to rapidly predict implant performance using data derived from high-fidelity FEA simulations. These simulations employed physics-faithful bone models with heterogeneous elasto-plastic material properties reconstructed from Computed Tomography (CT) scans of 16 dogs. The eXtended Finite Element Method (XFEM) was employed to capture crack initiation and propagation under 25 distinct loading scenarios, both with and without medullary conformal stabilization. Five ML models, including MLP, SVR, RF, XGBoost, and HistGBR were trained and evaluated using biological and morphometric features such as body weight, lesion location, bone length as well as 825 FEA simulation-derived crack-initiation loads as prediction targets. Hyperparameters were optimized via Bayesian tuning, and simulation-level stability was assessed across training-testing splits ranging from 50:50-90:10, while patient-level generalization was evaluated separately using nested Leave-One-Group-Out (LOGO) cross-validation. XGBoost demonstrated the best predictive performance on 165 held-out cases, achieving an average R2≈ 0.90 and a normalized mean absolute error of approximately 8%. Patient-level performance was more consistent for humeral cases than for tibial and radial cases, emphasizing the need for larger, bone-type-balanced datasets. Feature-importance analysis revealed lesion burden and body weight as dominant predictors, with anatomical scaling parameters (e.g., bone length, diaphyseal thickness) and density proxies contributing secondary effects, while sex and age showed negligible contributions within the current cohort. Retrospective clinical outcomes from six treated dogs were examined descriptively and provided preliminary clinical context rather than formal validation. FEA and surrogate predictions suggest that delayed fracture initiation can be achieved through intramedullary implant stabilization, although its effectiveness varies among patients. The proposed proof-of-concept framework provides a scalable, data-driven foundation for clinical decision support, with predictive accuracy expected to improve as additional outcome data become available.
