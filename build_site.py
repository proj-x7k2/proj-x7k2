# -----------------------------------------------------------------------
# build_site.py
#
# 이 파일이 하는 일 (초보자를 위한 설명):
#   website/template.html (틀)과 data/papers.json (내용)을 합쳐서,
#   website/index.html (실제로 여는 파일)을 새로 만듭니다.
#
#   이렇게 하면 웹사이트를 열 때 데이터를 따로 "요청"하지 않고 파일 안에
#   이미 들어있기 때문에, 서버 없이 그냥 더블클릭으로 열립니다.
#
#   run_weekly.sh가 요약을 끝낸 뒤 이 스크립트를 자동으로 실행해줍니다.
#   따로 손으로 실행할 필요는 없지만, 필요하면 다음처럼 실행할 수 있습니다:
#     python3 build_site.py
# -----------------------------------------------------------------------

import json
import os

import config

TEMPLATE_PATH = os.path.join("website", "template.html")
OUTPUT_PATH = os.path.join("website", "index.html")
PAPERS_JSON_PATH = os.path.join(config.DATA_DIR, "papers.json")

PLACEHOLDER = "/*__PAPERS_JSON__*/ []"


def build():
    if not os.path.exists(PAPERS_JSON_PATH):
        papers = []
    else:
        with open(PAPERS_JSON_PATH, "r", encoding="utf-8") as f:
            papers = json.load(f)

    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template = f.read()

    if PLACEHOLDER not in template:
        raise RuntimeError(
            f"website/template.html 안에서 '{PLACEHOLDER}' 를 찾을 수 없습니다. "
            "템플릿 파일이 손상되지 않았는지 확인하세요."
        )

    injected = template.replace(
        PLACEHOLDER,
        json.dumps(papers, ensure_ascii=False).replace("</", "<\\/"),
    )

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(injected)

    print(f"website/index.html 생성 완료 (논문 {len(papers)}편 포함)")


if __name__ == "__main__":
    build()
