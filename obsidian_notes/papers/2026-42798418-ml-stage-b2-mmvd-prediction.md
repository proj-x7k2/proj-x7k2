---
pmid: "42798418"
title: "Predicting stage B2 myxomatous mitral valve disease in dogs using machine learning and routine clinical data."
journal: "Frontiers in veterinary science"
year: "2026"
authors: ["Hasuk Nam", "Kyungchang Jeong", "Hanbit Seo", "Yeon Chae", "Byeong-Teck Kang", "Euijong Lee", "Taesik Yun", "Hakhyun Kim"]
doi: "10.1155/2016/4727054"
url: "https://pubmed.ncbi.nlm.nih.gov/42798418/"
study_type: "후향적 연구"
sample_size: "387"
species: ["dog"]
modality: ["radiography", "echocardiography"]
system: ["cardiovascular", "AI"]
topics: ["ai-imaging", "cardiac-imaging"]
tags: ["dog", "radiography", "echocardiography", "cardiovascular", "AI"]
evidence_basis: "abstract"
added_on: 2026-09-30
---
# Predicting stage B2 myxomatous mitral valve disease in dogs using machine learning and routine clinical data.

**Frontiers in veterinary science (2026)** · 후향적 연구, n=387 · [PubMed](https://pubmed.ncbi.nlm.nih.gov/42798418/) · DOI: 10.1155/2016/4727054
관련 주제: [[topics/ai-imaging]], [[topics/cardiac-imaging]]

## 국문 요약
Echocardiography가 개 stage B2 myxomatous mitral valve disease(MMVD) 진단의 gold standard이지만 2차 진료 현장에서는 장비·전문 인력 접근성이 제한적이라는 문제의식에서, echocardiography 없이 routine clinical data만으로 stage B2를 식별하는 머신러닝 모델을 개발했다. Client-owned 개 387마리(non-stage B2 252마리, stage B2 135마리)의 인구학적·혈액학적·혈청생화학적·요검사·흉부 방사선 변수를 이용해 gradient boosting 모델을 학습(80%)·검증(20%)한 결과, 정확도 0.825, 민감도 0.815, 특이도 0.830, ROC AUC 0.922로 높은 분류 성능을 보였다. 저자들은 이 모델이 echocardiography에 접근하기 어려운 상황에서 stage B2 조기 발견과 전문의 의뢰 판단을 도울 수 있다고 결론지었다.

## English summary
Although echocardiography is the gold standard for diagnosing stage B2 cardiac remodeling in canine myxomatous mitral valve disease (MMVD), it has limited availability and requires specialized expertise in general clinical settings. This study developed a machine learning model to identify dogs with stage B2 MMVD without echocardiography, using routine clinical data from 387 client-owned dogs (252 non-stage B2, 135 stage B2), including demographic, hematological, serum biochemical, urinalysis, and thoracic radiographic variables. A gradient boosting algorithm trained on 80% of the data and validated on the remaining 20% achieved an accuracy of 0.825, sensitivity of 0.815, specificity of 0.830, and an area under the ROC curve of 0.922. The authors concluded that this model could assist early detection and specialist referral of stage B2 disease when echocardiography is unavailable.

## 임상 시사점
Echocardiography 장비나 숙련된 판독 인력이 바로 없는 상황에서도, 흉부 방사선을 포함한 기본 혈액검사·요검사 결과를 종합하면 stage B2 MMVD 가능성이 높은 개를 선별해 심장 전문의·초음파 의뢰 우선순위를 정하는 데 참고할 수 있다. 다만 이는 echocardiography를 대체하는 확진 도구가 아니라 의뢰 여부를 돕는 선별 도구로 이해해야 한다.

## 연구 설계와 한계
Client-owned 개 387마리를 대상으로 한 후향적 연구로, echocardiography로 확진된 stage B2 여부를 기준(label)으로 삼아 비영상·영상(흉부 방사선) 변수를 결합한 gradient boosting 모델을 80/20으로 학습·검증했다. 단일 기관·단일 코호트의 내부 검증(internal validation)으로 보이며, 초록에는 외부 코호트 검증이나 흉부 방사선 변수 각각의 개별 기여도(feature importance)가 제시되지 않아 일반화 가능성은 추가 검증이 필요하다.

## 원문 초록
Early identification of Stage B2 myxomatous mitral valve disease in dogs is critical for initiating appropriate treatment to delay the onset of heart failure. Although echocardiography is the gold standard for diagnosing Stage B2 cardiac remodeling, it has limitations in general clinical settings owing to the limited availability of specialized equipment and the need for advanced technical expertise. We developed a machine learning model using routine clinical data to identify dogs with Stage B2 disease without echocardiography. A total of 387 client-owned dogs (252 non-Stage B2 dogs and 135 Stage B2 dogs) were evaluated. A gradient boosting algorithm was trained on 80% of the data and validated on a test dataset comprising the remaining 20%, incorporating demographic, hematological, serum biochemical, urinalysis, and thoracic radiographic variables. The model achieved an accuracy of 0.825 [95% confidence interval (CI): 0.738-0.900], a sensitivity of 0.815 (95% CI: 0.650-0.957), a specificity of 0.830 (95% CI: 0.729-0.919), and an area under the receiver operating characteristic curve of 0.922 (95% CI: 0.860-0.971). These findings demonstrate that machine learning can accurately classify Stage B2 status using routine clinical data, thereby assisting veterinary clinicians in the early detection and specialist referral when echocardiography is unavailable.
