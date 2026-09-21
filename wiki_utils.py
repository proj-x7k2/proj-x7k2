# -----------------------------------------------------------------------
# wiki_utils.py
# 여러 스크립트가 같이 쓰는 도우미 함수 모음입니다. 직접 실행하지 않습니다.
#
# 핵심: 논문 페이지(obsidian_notes/papers/*.md) 맨 위의 메타데이터(frontmatter)를
# 읽는 함수. 이 메타데이터가 "진실의 원천"이고, 웹사이트용 papers.json은
# 여기서 자동으로 만들어집니다.
# -----------------------------------------------------------------------

import json
import os
import re

import config

PAPERS_DIR = os.path.join(config.OBSIDIAN_DIR, "papers")
TOPICS_DIR = os.path.join(config.OBSIDIAN_DIR, "topics")


def _parse_value(raw):
    raw = raw.strip()
    if raw == "":
        return ""
    try:
        return json.loads(raw)          # "문자열", [목록], 숫자 등
    except (json.JSONDecodeError, ValueError):
        return raw.strip('"').strip("'")  # 따옴표 없는 값(예: 2026-09-21)


def parse_frontmatter(text):
    """마크다운 맨 앞의 --- ... --- 블록을 딕셔너리로, 나머지를 본문으로 돌려줍니다."""
    if not text.startswith("---"):
        return {}, text
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.DOTALL)
    if not match:
        return {}, text
    meta = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = _parse_value(value)
    return meta, match.group(2)


def extract_section(body, heading):
    """본문에서 '## {heading}' 아래부터 다음 '## ' 전까지를 꺼냅니다 (### 소제목은 유지)."""
    pattern = rf"^##\s+{re.escape(heading)}\s*\n(.*?)(?=^##\s+|\Z)"
    match = re.search(pattern, body, re.DOTALL | re.MULTILINE)
    return match.group(1).strip() if match else ""


def iter_paper_pages():
    """(파일경로, 메타데이터, 본문) 을 논문 페이지마다 돌려줍니다."""
    if not os.path.isdir(PAPERS_DIR):
        return
    for name in sorted(os.listdir(PAPERS_DIR)):
        if not name.endswith(".md"):
            continue
        path = os.path.join(PAPERS_DIR, name)
        with open(path, "r", encoding="utf-8") as f:
            meta, body = parse_frontmatter(f.read())
        yield path, meta, body


def processed_pmids():
    """위키 페이지가 이미 있는 논문 + 의도적으로 건너뛴 논문의 PMID 집합."""
    pmids = set()
    for _, meta, _ in iter_paper_pages() or []:
        if meta.get("pmid"):
            pmids.add(str(meta["pmid"]))
    skipped_path = os.path.join(config.DATA_DIR, "skipped.json")
    if os.path.exists(skipped_path):
        try:
            with open(skipped_path, "r", encoding="utf-8") as f:
                for item in json.load(f):
                    pmid = item.get("pmid") if isinstance(item, dict) else item
                    if pmid:
                        pmids.add(str(pmid))
        except (json.JSONDecodeError, OSError):
            pass
    return pmids
