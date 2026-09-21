# -----------------------------------------------------------------------
# build_site.py
# 위키(obsidian_notes/)에서 papers.json, topics.json 을 만들고, 이를
# website/template.html 에 넣어 website/index.html 을 완성합니다.
# (서버 없이 더블클릭으로 열리는 단일 파일)
#   python3 build_site.py
# -----------------------------------------------------------------------

import json
import os

from build_papers import build as build_papers
from build_topics import build as build_topics

TEMPLATE_PATH = os.path.join("website", "template.html")
OUTPUT_PATH = os.path.join("website", "index.html")


def build():
    papers = build_papers()
    topics = build_topics()

    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template = f.read()

    for placeholder, data in {"/*__PAPERS_JSON__*/ []": papers,
                              "/*__TOPICS_JSON__*/ []": topics}.items():
        if placeholder not in template:
            raise RuntimeError(f"website/template.html 안에 '{placeholder}' 가 없습니다.")
        template = template.replace(
            placeholder, json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(template)
    print(f"website/index.html 생성 완료 (논문 {len(papers)}편, 주제 {len(topics)}개)")


if __name__ == "__main__":
    build()
