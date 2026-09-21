# -----------------------------------------------------------------------
# build_topics.py
# obsidian_notes/topics/*.md (주제별 종합 페이지)를 읽어 웹사이트용
# data/topics.json 을 만듭니다. build_site.py가 자동으로 실행합니다.
# -----------------------------------------------------------------------

import json
import os
import re

import config
from wiki_utils import TOPICS_DIR, extract_section, parse_frontmatter

OUTPUT_PATH = os.path.join(config.DATA_DIR, "topics.json")


def _parse_related_papers(section_text):
    notes = []
    for line in section_text.splitlines():
        line = line.strip()
        if not line.startswith("-"):
            continue
        match = re.match(r"-\s*\[\[(.*?)\]\]\s*[—–-]?\s*(.*)", line)
        note = match.group(2).strip() if match else line.lstrip("- ").strip()
        if note:
            notes.append(note)
    return notes


def parse_topic_file(path, slug):
    with open(path, "r", encoding="utf-8") as f:
        meta, body = parse_frontmatter(f.read())
    title_match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    related = _parse_related_papers(extract_section(body, "관련 논문"))
    return {
        "slug": slug,
        "title": meta.get("title") or (title_match.group(1).strip() if title_match else slug),
        "synthesis": extract_section(body, "현재까지의 종합"),
        "related_papers": related,
        "paper_count": len(related),
        "conflicting_evidence": extract_section(body, "상충되는 근거"),
        "open_questions": extract_section(body, "남은 질문"),
    }


def build():
    topics = []
    if os.path.isdir(TOPICS_DIR):
        for filename in sorted(os.listdir(TOPICS_DIR)):
            if filename.endswith(".md"):
                topics.append(parse_topic_file(os.path.join(TOPICS_DIR, filename), filename[:-3]))
    topics.sort(key=lambda t: t["paper_count"], reverse=True)
    os.makedirs(config.DATA_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(topics, f, ensure_ascii=False, indent=2)
    print(f"data/topics.json 생성 완료 (주제 {len(topics)}개)")
    return topics


if __name__ == "__main__":
    build()
