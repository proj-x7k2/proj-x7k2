# -----------------------------------------------------------------------
# config.py
# 이 파일은 "설정값"만 모아둔 곳입니다. 코드를 몰라도 이 파일의 값만
# 바꾸면 검색 조건을 조정할 수 있습니다.
# -----------------------------------------------------------------------

# 1) PubMed에서 검색할 키워드 목록
#    - 여기 적힌 단어 중 하나라도 논문 제목/초록에 포함되면 검색됩니다.
#    - 필요한 만큼 자유롭게 추가/삭제하세요 (쉼표로 구분).
KEYWORDS = [
    "veterinary radiology",
    "veterinary MRI",
    "veterinary CT",
    "veterinary ultrasound",
    "veterinary diagnostic imaging",
]

# 2) 우선적으로 챙기고 싶은 저널 이름
#    - 참고: 지금 버전에서는 검색 조건에 실제로 쓰이지 않습니다 (키워드로만
#      검색합니다). 저널 이름만으로 필터링하면 주제와 상관없는 논문까지
#      다 걸려서 위키가 지저분해지기 때문입니다. 나중에 필요하면 다시
#      활용할 수 있도록 목록만 남겨둡니다.
JOURNALS = [
    "Veterinary Radiology & Ultrasound",
    "Veterinary Surgery",
    "Journal of the American Veterinary Medical Association",
    "Journal of Veterinary Internal Medicine",
    "Frontiers in Veterinary Science",
]

# 2-1) 저널 자체가 영상의학 전문지라서, 키워드와 상관없이 실린 논문을
#      전부 가져와도 되는 저널 목록입니다 (위 JOURNALS와 다르게 실제로
#      검색 조건에 쓰입니다). JAVMA처럼 다양한 분야를 다루는 종합지는
#      여기 넣지 마세요 — 주제 무관한 논문까지 다 들어옵니다.
FULL_COVERAGE_JOURNALS = [
    "Veterinary Radiology & Ultrasound",
]

# 2-2) 소동물(개·고양이·토끼) 진료에 맞춰, 대동물/산업동물이 주제인
#      논문은 제외합니다. 여기 적힌 단어 중 하나라도 제목/초록에
#      있으면 검색 결과에서 빠집니다. 말·소 진료도 함께 보시게 되면
#      이 목록을 비워두거나(= 제외 안 함) 필요 없는 항목만 지우세요.
EXCLUDE_SPECIES = [
    "equine", "horse", "foal",
    "bovine", "cattle", "cow", "calf",
    "porcine", "swine", "pig",
    "ovine", "sheep", "caprine", "goat",
    "camelid", "llama", "alpaca",
    "poultry", "avian",  # 조류는 소동물 진료 범위 밖이면 유지, 진료하시면 이 줄 삭제
    "livestock", "farm animal",
]

# 3) 최근 며칠 이내에 발표된 논문을 가져올지
#    - 매주 1회 실행한다면 7~10 정도가 적당합니다.
DAYS_BACK = 7

# 4) 한 번 실행할 때 최대 몇 편까지 가져올지 (진짜 상한선입니다 — 이 숫자를
#    넘는 나머지는 다음에도 다시 안 나타나니, 넉넉하게 잡아두는 걸 추천합니다.
#    숫자를 늘리면 그만큼 Claude Code 요약 시간이 오래 걸릴 뿐, 비용은
#    늘지 않습니다 — 구독 사용량으로 처리되기 때문입니다.)
MAX_RESULTS = 100

# 5) 결과가 저장될 폴더 (보통 건드릴 필요 없음)
DATA_DIR = "data"
OBSIDIAN_DIR = "obsidian_notes"
