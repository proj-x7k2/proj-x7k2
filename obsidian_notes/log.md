# 변경 기록

## 2026-09-30 수집 (2)
- `data/raw_papers.json`의 논문 6편 중 4편 처리, 2편 건너뜀.
- 건너뜀 (모두 `data/skipped.json`에 기록):
  - `42797913`(KLH 기반 다중요법을 받은 개 추정 urothelial carcinoma 2예 장기 추적) — CT·초음파는 치료 경과 추적 모니터링 지표로만 부수적 사용.
  - `42797899`(토끼 median sternotomy에서 초음파 유도 양측 TTP block) — 초음파는 신경차단 시행 보조 도구로만 사용.
- 신규 논문 4편 페이지 생성 및 주제 통합:
  - `42801331`(개 idiopathic cholesterol pericarditis, echocardiography·CT로 종양·감염 원인 배제 후 확진) → `cardiac-imaging`.
  - `42775486`(개 iliosacral lymph node 정상 CT 참고치, RECIST v1.1 적용 시 MinTD 권장) → 신규 주제 `oncologic-imaging` 생성.
  - `42797900`(건강한 Beagle의 작은 voxel SVS vs MVS proton MRS 비교, SVS가 촬영시간 단축) → `neuro-imaging`.
  - `42797884`(MRI 정상인 idiopathic epilepsy 고양이의 interictal 1H-MRS, 우측 temporal lobe NAA/tCr 저하) → `neuro-imaging`.
- 신설 주제: `oncologic-imaging` (CLAUDE.md 기존 주제 체계 표에 있던 항목, 이번에 첫 논문 유입).
- `raw/pdf/` 폴더 자체가 없어 워크플로우 B(전문 반영) 해당 사항 없음.
- `overview.md` 주제 목록·논문 수를 갱신: `cardiac-imaging` 7→8편, `neuro-imaging` 5→7편, `oncologic-imaging` 신설 1편.

## 2026-09-30 수집
- `data/raw_papers.json`의 논문 10편 중 6편 처리, 4편 건너뜀.
- 건너뜀 (모두 `data/skipped.json`에 기록):
  - `42797985`(개 응급 개복술 시 초음파 유도 국소마취 블록 비교) — 초음파는 신경차단 시행 보조 도구로만 사용.
  - `42797984`(고양이 척추 외상의 진단적 해부 소견과 치료·회복) — 방사선은 병변 국소화·수술 계획용으로만 부수적 사용, 핵심은 임플란트 선택과 수술 결과.
  - `42787157`(TPLO+ACS 병합요법의 개 CCLR 기능회복·OA 진행 억제) — 방사선 OA 등급은 여러 평가지표 중 하나로 부수적 사용.
  - `42791690`(개 전립선비대증 등급화 설문·웹 기반 증상지수 개발) — 초음파는 언급 수준, 핵심은 증상지수(ZSI) 개발.
- 신규 논문 6편 페이지 생성 및 주제 통합:
  - `42797990`(고양이 TMJ static vs kinematic MRI, dislocation 시 inclination angle 유의 변화) → 신규 주제 `head-neck-imaging` 생성.
  - `42798418`(routine clinical data+흉부 방사선 기반 gradient boosting으로 stage B2 MMVD 식별, AUC 0.922) → `ai-imaging` + `cardiac-imaging` (2개 주제).
  - `42791713`(강아지 ulna aneurysmal bone cyst, 임상 호전에도 방사선상 진행 후 재수술) → `musculoskeletal-imaging`.
  - `42791699`(CTA·echocardiography 기반 환자맞춤형 CFD로 개 pulmonic stenosis 폐동맥 혈류역학 분석) → `cardiac-imaging`.
  - `42781373`(고양이 cervical vertebral vascular hamartoma, 반복 영상·수술로 재성장 확인) → `spinal-imaging` + `vascular-imaging` (2개 주제).
  - `42791684`(개 acute prostatitis 35예 초음파 소견, abscess 71%에서 확인) → `urogenital-imaging`.
- 신설 주제: `head-neck-imaging` (CLAUDE.md 기존 주제 체계 표에 있던 항목, 이번에 첫 논문 유입).
- 이전 실행(2026-09-29)에서 페이지만 생성되고 미커밋 상태였던 4편(`42803120`, `42786736`, `42770669`, `42772030`)은 주제 페이지 통합·역링크가 이미 완료되어 있어 추가 작업 없음.
- `raw/pdf/` 폴더 자체가 없어 워크플로우 B(전문 반영) 해당 사항 없음.
- `overview.md` 주제 목록·논문 수를 갱신: `musculoskeletal-imaging` 11→12편, `cardiac-imaging` 5→7편, `ai-imaging` 4→5편, `spinal-imaging` 2→3편, `urogenital-imaging` 3→4편, `vascular-imaging` 1→2편, `head-neck-imaging` 신설 1편.

## 2026-09-29 수집
- `data/raw_papers.json`의 논문 10편 중 4편 처리, 6편 건너뜀.
- 건너뜀 (모두 `data/skipped.json`에 기록):
  - `42806563`(고양이 AS-OCT Descemet's membrane detachment 증례) — 안과 OCT 영상, modality(OCT)·주제 체계(안과) 모두 범위 밖.
  - `42804870`(개·고양이 비수술적 남성 피임 전략 종설) — 영상의학과 무관.
  - `42800182`(aglepristone 자궁축농증 치료 다기관 임상연구) — 경복부 초음파는 치료반응 모니터링 지표로만 부수적 사용.
  - `42779179`(고양이 undenatured type II collagen 보충제의 기동성 개선 RCT) — 방사선검사는 DJD 진단 확인용으로만 부수적 사용.
  - `42798028`(개 hemilaminectomy 시 ESP vs RM block 진통 요구량 비교) — 초음파는 신경차단 시행 보조 도구로만 사용.
  - `42791785`(Vitcone vs Vi 잠금판 시스템 요골·척골 골절 고정 비교) — 방사선 유합평가는 여러 평가지표 중 하나로 부수적 사용.
- 신규 논문 4편 페이지 생성 및 주제 통합:
  - `42803120`(고양이 200마리 중 99.5%에서 left ventricular band 확인) → `cardiac-imaging`.
  - `42786736`(고양이 meningioma 4예의 pseudocystic fluid accumulation, microcystic형 첫 보고) → `neuro-imaging`.
  - `42770669`(CVC 침범 HCC 개 2마리, staged CVC occlusion 후 en bloc hepatectomy) → 신규 주제 `vascular-imaging` 생성 + `abdominal-imaging` (2개 주제).
  - `42772030`(건강한 고양이 고환 2D-SWE 기준값) → `urogenital-imaging`.
- 신설 주제: `vascular-imaging` (CLAUDE.md 기존 주제 체계 표에 있던 항목, 이번에 첫 논문 유입).
- `raw/pdf/` 폴더 자체가 없어 워크플로우 B(전문 반영) 해당 사항 없음.
- `overview.md` 주제 목록·논문 수를 갱신: `abdominal-imaging` 5→6편, `cardiac-imaging` 4→5편, `neuro-imaging` 4→5편, `urogenital-imaging` 2→3편, `vascular-imaging` 신설 1편.

## 2026-09-22 수집 (2)
- `data/raw_papers.json`의 논문 9편 중 8편 처리, 1편 건너뜀.
- 건너뜀: `42738489`(사쿠비트릴/발사르탄+hydrochlorothiazide로 고양이 refractory cardiogenic pleural effusion 장기 조절 증례) — echocardiography는 기저 심장병 서술에만 부수적으로 사용되고 연구 핵심은 약물 치료 경과라 제외, `data/skipped.json`에 기록.
- 신규 논문 8편 페이지 생성 및 주제 통합:
  - `42757221`(외상 의심 vaginal atresia에 의한 hydrocolpos, CT·vaginoscopy·retrograde cystography로 진단) → `urogenital-imaging`.
  - `42738496`(조영 CT 후 순차적 지연영상에서 중증 조영제 과민반응 진행) → `imaging-technique-safety`.
  - `42725102`(흉수 압박성 낭성 병변이 염증성 meningoproliferative disorder로 확인된 첫 증례) → 신규 주제 `spinal-imaging` 생성.
  - `42722611`(mitral-to-aortic VTI ratio로 개 MMVD의 MR 중증도 평가) → `cardiac-imaging`.
  - `42760156`(개 MMVD 1108마리의 mitral valve leaflet 형태학적 분류와 stage 연관성) → `cardiac-imaging`.
  - `42710340`(토끼 propofol 단독 vs propofol+dextroketamine 유도의 심초음파·혈압 효과) → `cardiac-imaging` + `sedation-restraint-imaging` (2개 주제).
  - `42724435`(FISS 유사 sarcoma의 perineural spread를 통한 척수 침범 첫 증례) → `spinal-imaging`.
  - `42765741`(고양이 EEG-fMRI로 epileptogenic zone 국소화 방법론 pilot study) → `neuro-imaging`.
- 신설 주제: `spinal-imaging` (CLAUDE.md 기존 주제 체계 표에 있던 항목, 이번에 첫 논문 유입).
- `raw/pdf/` 폴더 자체가 없어 워크플로우 B(전문 반영) 해당 사항 없음.
- `overview.md` 주제 목록·논문 수를 갱신: `cardiac-imaging` 1→4편, `imaging-technique-safety` 4→5편, `neuro-imaging` 3→4편, `urogenital-imaging` 1→2편, `sedation-restraint-imaging` 1→2편, `spinal-imaging` 신설 2편.

## 2026-09-22 수집
- 논문 10편 처리, 건너뜀 0편.
- `data/raw_papers.json`의 10편 중 5편(42705596, 42710191, 42746025, 42759150, 42761083)은 이미 논문 페이지가 있었으나 `topics` 프론트매터의 주제 페이지 통합·역링크가 빠져 있어 마무리함:
  - `ai-imaging`에 42705596(CT-FEA-ML 골절 하중 예측)·42746025(canine glioma radiomics) 통합 — "영상 기반 정량 예측 모델" 소제목 신설.
  - `imaging-technique-safety`에 42761083(elbow CT 체위 비교) 통합 — "환자 체위와 영상 품질" 소제목 신설.
  - 신규 주제 페이지 2개 생성(첫 논문 프론트매터에는 있었으나 파일이 없었음): `thoracic-imaging`(42710191), `urogenital-imaging`(42759150).
- 신규 논문 5편 페이지 생성 및 주제 통합:
  - `42750099`(동맥혈 채혈법에 따른 흉부 CT atelectasis 차이) → `imaging-technique-safety`.
  - `42735743`(성장기 소형견 심초음파 allometric 참고치) → 신규 주제 `cardiac-imaging` 생성.
  - `42738595`(대규모 동물 방임 현장 forensic MNI 감정, postmortem radiography 포함) → `trauma-forensic-imaging`.
  - `42767266`(고양이 Zurich Mini cementless THR, 방사선 추적 결과) → `musculoskeletal-imaging`.
  - `42765932`(3D 프린팅 hepatic artery 팬텀 CT bolus tracking 훈련) → `imaging-technique-safety`.
- 신설 주제: `cardiac-imaging`, `thoracic-imaging`, `urogenital-imaging` (모두 CLAUDE.md 기존 주제 체계 표에 있던 항목).
- `raw/pdf/`에 PDF 없어 워크플로우 B(전문 반영) 해당 사항 없음.
- `overview.md` 주제 목록·논문 수를 실제 상태(주제 10개, 총 33개 논문-주제 연결)에 맞춰 전면 갱신.

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
