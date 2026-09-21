---
pmid: "42746025"
title: "Radiomics and comparative neuroimaging of canine gliomas and human glioblastomas: a step toward precision medicine."
journal: "Frontiers in veterinary science"
year: "2026"
authors: ["Ricardo Faustino", "Joaquim Henriques"]
doi: "10.1007/s00330-023-09827-2"
url: "https://pubmed.ncbi.nlm.nih.gov/42746025/"
study_type: "후향적 연구"
sample_size: ""
species: ["dog"]
modality: ["MRI"]
system: ["neuro", "oncology", "AI"]
topics: ["neuro-imaging", "ai-imaging"]
tags: ["dog", "MRI", "neuro", "oncology", "AI"]
evidence_basis: "abstract"
added_on: 2026-09-21
---
# Radiomics and comparative neuroimaging of canine gliomas and human glioblastomas: a step toward precision medicine.

**Frontiers in veterinary science (2026)** · 후향적 연구, n="" (초록에 개별 canine glioma 증례 수 미기재) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/42746025/) · DOI: 10.1007/s00330-023-09827-2
관련 주제: [[topics/neuro-imaging]] · [[topics/ai-imaging]]

## 국문 요약
Brachycephalic 견종에서 호발하는 canine glioma가 사람 glioblastoma와 생물학적·임상적 유사성을 공유한다는 점에 착안해, T2-weighted FLAIR MRI에서 radiomics(texture, shape, intensity) 특징을 추출해 canine glioma와 human glioblastoma를 비교했다. 선별된 radiomic feature("jointaverage", "autocorrelation" 등)는 종양 조직과 비병변 조직을 AUC 80% 이상으로 구별했고, SVM 모델은 개·사람 데이터셋을 통합해 종양 대 비병변 조직 판별에서 80.33%의 정확도를 보였다. 저자들은 canine glioma가 human glioblastoma 연구를 위한 translational model로서 가치가 있다고 결론지었으나, 표본 크기와 집단 다양성의 한계로 대규모 코호트에서의 검증이 필요하다고 밝혔다.

## English summary
Motivated by the biological and clinical similarities between brachycephalic-predisposed canine gliomas and human glioblastomas, this study extracted radiomic features (texture, shape, intensity) from T2-weighted FLAIR MRI to compare canine glioma and human glioblastoma imaging. Selected radiomic features (e.g., "jointaverage", "autocorrelation") discriminated tumoral from non-lesioned tissue with ROC AUC values above 80%, and an SVM model achieved 80.33% accuracy distinguishing gliomas/glioblastomas from non-lesioned brain tissue across the combined canine-human dataset. The authors conclude canine gliomas represent a valuable translational model for human glioblastoma research, while noting that limited sample size and population diversity require validation in larger cohorts.

## 임상 시사점
초록 기준으로는 이 연구가 임상 진단 프로토콜을 곧바로 제시하지는 않으며, brachycephalic 견종의 glioma 의심 MRI 판독 시 T2-FLAIR 기반 radiomics가 향후 정량적 보조 지표로 발전할 가능성이 있다는 정도로만 참고할 수 있다 — 제한적 근거.

## 연구 설계와 한계
Canine glioma와 human glioblastoma의 MRI(T2-FLAIR) 데이터를 함께 분석한 비교·translational 영상 연구로, 개별 canine glioma 증례 수·영상 확보 시점(전향적/후향적 여부)이 초록에 명시되어 있지 않아 후향적 영상 분석으로 추정했다. 저자 스스로 "limited sample size and population diversity"를 한계로 명시했고, 사람 데이터와 통합한 분석 특성상 canine 단독 진단 성능(민감도·특이도 등)은 별도로 제시되지 않았다. 임상 적용을 위한 전향적·대규모 검증이 필요하다.

## 원문 초록
INTRODUCTION: Gliomas are primary Central Nervous System glial tumors common in dogs and humans. Human glioblastomas are the most aggressive subtype, with an average survival of 15 months after diagnosis. Brachycephalic dogs are predisposed to gliomas and share biological and clinical features with human glioblastomas. This study explored radiomics applied to T2 weigthed Fluid Attenuated Inversion Recovery (T2-FLAIR) magnetic resonance imaging (MRI) sequences to characterize canine glioma lesions and non-lesioned tissues, aiming to identify imaging biomarkers for diagnosis and prognosis.

METHODS: MRI scans from canine gliomas and human glioblastomas were analyzed. Regions of Interest (ROIs) were segmented for extraction of radiomic features including texture, shape, and intensity. Descriptive and non-parametric statistical analyses, ANOVA, and Receiver Operating Characteristic (ROC) curves were used to evaluate feature discrimination capacity, particularly features with area under the curve (AUC) values above 80%, such as "jointaverage" and "autocorrelation".

RESULTS: Volumetric analysis revealed significant differences between groups (p < 0.001). Selected radiomic features discriminated tumoral from non-lesioned tissues, with ROC AUC values exceeding 80% (p < 0.001). The Support Vector Machine (SVM) model achieved 80.33% accuracy in distinguishing gliomas and glioblastomas from non-lesioned brain tissue across canine and human datasets.

DISCUSSION: Radiomic features revealed comparable texture patterns between canine gliomas and human glioblastomas, enabling cross-species discrimination between tumoral and non-lesioned tissue with AUC values above 80% and SVM accuracy of 80.33%. These findings support canine gliomas as a valuable translational model for human glioblastoma research and precision medicine. However, the limited sample size and population diversity require validation in larger cohorts.

CONCLUSION: Consistent imaging biomarkers across canine gliomas and human glioblastomas support advances in comparative and translational medicine. Radiomic features extracted from T2-FLAIR MRI enabled non-invasive discrimination between tumoral and non-lesioned brain tissue across species, reinforcing the relevance of canine gliomas as a natural model for human glioblastoma and the potential of comparative neuroimaging for precision medicine.
