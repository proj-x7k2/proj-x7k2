# -----------------------------------------------------------------------
# config.py
# 이 파일은 "설정값"만 모아둔 곳입니다. 코드를 몰라도 이 파일의 값만
# 바꾸면 검색 조건을 조정할 수 있습니다.
#
# 검색 구조 (v2):
#   (영상 기법 용어 OR 영상 전문 저널)
#   AND (개·고양이·토끼)
#   AND (수의학 맥락: 수의학 저널이거나 초록에 veterinary 등이 있음)
#   + 날짜는 "PubMed에 새로 등록된 날짜" 기준
#
# 참고: 새로 등록된 논문은 MeSH 색인이 몇 주 늦게 붙기 때문에, MeSH만으로
# 검색하면 최신 논문을 놓칩니다. 그래서 [tiab](제목/초록 단어)를 함께 씁니다.
# -----------------------------------------------------------------------

# 1) 영상 기법 용어 (하나라도 해당되면 "영상 논문" 후보)
#    주의: "CT" 단독은 넣지 않았습니다 — PCR의 Ct 값 등과 헷갈려 잡음이 많습니다.
IMAGING_TERMS = [
    '"Diagnostic Imaging"[MeSH]',
    'radiograph*[tiab]',
    'radiology[tiab]',
    '"computed tomography"[tiab]',
    '"computed tomographic"[tiab]',
    '"CT angiography"[tiab]',
    '"magnetic resonance"[tiab]',
    'MRI[tiab]',
    'ultrasonograph*[tiab]',
    'ultrasound[tiab]',
    'sonograph*[tiab]',
    'echocardiograph*[tiab]',
    'fluoroscop*[tiab]',
    'scintigraph*[tiab]',
    '"positron emission"[tiab]',
    'elastograph*[tiab]',
]

# 2) 영상 전문 저널: 여기 실린 논문은 위 용어가 없어도 후보로 포함합니다.
FULL_COVERAGE_JOURNALS = [
    "Veterinary Radiology & Ultrasound",
]

# 3) 대상 종 (소동물 진료 범위). 여기 없는 종만 다루는 논문은 검색되지 않습니다.
#    주의: "cat*" 같은 와일드카드는 catheter까지 잡으므로 쓰지 않았습니다.
SPECIES_TERMS = [
    '"Dogs"[MeSH]', 'dog[tiab]', 'dogs[tiab]', 'canine[tiab]',
    '"Cats"[MeSH]', 'cat[tiab]', 'cats[tiab]', 'feline[tiab]',
    '"Rabbits"[MeSH]', 'rabbit[tiab]', 'rabbits[tiab]',
]

# 4) 수의학 맥락 (실험동물 모델 연구 = 사람 질환 연구용 개/토끼 실험을 줄이기 위함)
#    수의학 저널에 실렸거나, 초록에 수의학 진료 맥락이 드러나면 통과합니다.
VET_CONTEXT_TERMS = [
    'veterinar*[tiab]',
    '"client-owned"[tiab]',
    '"client owned"[tiab]',
    '"small animal"[tiab]',
    '"companion animal"[tiab]',
    '"companion animals"[tiab]',
]
VET_JOURNALS = [
    "Veterinary Radiology & Ultrasound",
    "Journal of Veterinary Internal Medicine",
    "Journal of the American Veterinary Medical Association",
    "Veterinary Surgery",
    "Frontiers in Veterinary Science",
    "Journal of Small Animal Practice",
    "Journal of Feline Medicine and Surgery",
    "Journal of Veterinary Cardiology",
    "Veterinary Journal (London, England : 1997)",
    "The Veterinary Record",
    "BMC Veterinary Research",
    "Journal of Veterinary Science",
    "Veterinary and Comparative Oncology",
    "Veterinary Ophthalmology",
    "Journal of the American Animal Hospital Association",
    "American Journal of Veterinary Research",
    "Veterinary and Comparative Orthopaedics and Traumatology : V.C.O.T",
    "Journal of Veterinary Emergency and Critical Care (San Antonio, Tex. : 2001)",
    "Topics in Companion Animal Medicine",
    "Journal of Exotic Pet Medicine",
]

# 5) 검색 기간: PubMed에 "등록된 날짜" 기준으로 최근 며칠
#    - 매주 실행 + 14일이면, 한 주를 통째로 놓쳐도 다음 주에 자동으로 따라잡습니다.
#    - 이미 처리한 논문은 다시 처리하지 않으므로 겹쳐도 비용이 늘지 않습니다.
DAYS_BACK = 14

# 6) 한 번 실행할 때 최대 몇 편까지 넘길지.
#    넘친 나머지는 "처리 완료"로 표시되지 않으므로, 다음 주에 다시 후보로 잡힙니다.
#    (구독 사용량 한도를 고려해 한 번에 너무 많이 넘기지 않도록 60으로 둡니다)
MAX_RESULTS = 60

# 7) 폴더 (보통 건드릴 필요 없음)
DATA_DIR = "data"
RAW_DIR = "raw"            # 원자료 층: raw/pubmed/{pmid}.json, raw/pdf/*.pdf
OBSIDIAN_DIR = "obsidian_notes"
