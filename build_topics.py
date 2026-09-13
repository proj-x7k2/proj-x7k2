# -----------------------------------------------------------------------
# build_topics.py
#
# 이 파일이 하는 일 (초보자를 위한 설명):
#   obsidian_notes/topics/ 안의 마크다운 파일들(주제별 종합 페이지)을 읽어서,
#   웹사이트가 쓸 수 있는 형태(data/topics.json)로 변환합니다.
#
#   CLAUDE.md에 정의된 "주제 페이지 형식"(# 제목, ## 현재까지의 종합,
#   ## 관련 논문, ## 상충되는 근거)을 그대로 읽어서 각 섹션을 추출합니다.
#   따로 손으로 실행할 필요는 없습니다 — build_site.py가 자동으로 이 스크립트를
#   함께 실행합니다.
# -----------------------------------------------------------------------

import json
import os
import re

import config

TOPICS_DIR = os.path.join(config.OBSIDIAN_DIR, "topics")
OUTPUT_PATH = os.path.join(config.DATA_DIR, "topics.json")


def _extract_section(content, heading):
    """마크다운 안에서 '## {heading}' 다음부터 다음 '##' 전까지의 내용을 꺼냅니다."""
    pattern = rf"##\s+{re.escape(heading)}\s*\n(.*?)(?=\n##\s+|\Z)"
    match = re.search(pattern, content, re.DOTALL)
    return match.group(1).strip() if match else ""


def _parse_related_papers(section_text):
    """'## 관련 논문' 섹션의 각 줄(- [[papers/...]] — 설명)에서 설명 부분만 꺼냅니다."""
    notes = []
    for line in section_text.splitlines():
        line = line.strip()
        if not line.startswith("-"):
            continue
        match = re.match(r"-\s*\[\[.*?\]\]\s*—?\s*(.*)", line)
        note = match.group(1).strip() if match else line.lstrip("- ").strip()
        if note:
            notes.append(note)
    return notes


def parse_topic_file(path, slug):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else slug

    synthesis = _extract_section(content, "현재까지의 종합")
    related_section = _extract_section(content, "관련 논문")
    conflicting = _extract_section(content, "상충되는 근거")
    related_papers = _parse_related_papers(related_section)

    return {
        "slug": slug,
        "title": title,
        "synthesis": synthesis,
        "related_papers": related_papers,
        "paper_count": len(related_papers),
        "conflicting_evidence": conflicting,
    }


def build():
    topics = []

    if os.path.isdir(TOPICS_DIR):
        for filename in sorted(os.listdir(TOPICS_DIR)):
            if not filename.endswith(".md"):
                continue
            slug = filename[:-3]
            path = os.path.join(TOPICS_DIR, filename)
            topics.append(parse_topic_file(path, slug))

    # 관련 논문이 많은 주제부터 보이도록 정렬
    topics.sort(key=lambda t: t["paper_count"], reverse=True)

    os.makedirs(config.DATA_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(topics, f, ensure_ascii=False, indent=2)

    print(f"data/topics.json 생성 완료 (주제 {len(topics)}개)")
    return topics


if __name__ == "__main__":
    build()
