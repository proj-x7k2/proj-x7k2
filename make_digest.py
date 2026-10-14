# -----------------------------------------------------------------------
# make_digest.py — 주간 다이제스트 준비·마무리 (run_weekly.sh가 사용)
#
#   --snapshot   실행 전 위키에 있던 논문 목록을 기록
#   --prepare    실행 후 새로 추가된 논문을 data/digest_input.json 에 정리 (편수 출력)
#   --fallback   Claude가 다이제스트를 못 썼으면 기본 목록으로 대신 작성
#   --issue URL  GitHub 알림(Issue)용 본문을 만듦 (위키 링크 → PubMed 링크로 변환)
# -----------------------------------------------------------------------
import json
import os
import re
import sys
from datetime import date

import config

PAPERS_JSON = os.path.join(config.DATA_DIR, "papers.json")
TOPICS_JSON = os.path.join(config.DATA_DIR, "topics.json")
SNAPSHOT = os.path.join("logs", "before_pmids.json")
INPUT = os.path.join(config.DATA_DIR, "digest_input.json")
ISSUE_BODY = os.path.join(config.DATA_DIR, "digest_issue.md")
ISSUE_TITLE = os.path.join(config.DATA_DIR, "digest_issue_title.txt")
DIGEST_DIR = os.path.join(config.OBSIDIAN_DIR, "digests")


def _load(path, default):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        return default


def snapshot():
    os.makedirs("logs", exist_ok=True)
    pmids = [p["pmid"] for p in _load(PAPERS_JSON, [])]
    with open(SNAPSHOT, "w", encoding="utf-8") as f:
        json.dump(pmids, f)


def prepare():
    before = set(_load(SNAPSHOT, []))
    papers = [p for p in _load(PAPERS_JSON, []) if p["pmid"] not in before]
    if not os.path.exists(SNAPSHOT) or not papers:
        if os.path.exists(INPUT):
            os.remove(INPUT)
        print(0)
        return
    today = date.today().isoformat()
    data = {
        "date": today,
        "output_path": os.path.join(DIGEST_DIR, f"{today}.md"),
        "count": len(papers),
        "papers": [{k: p.get(k, "") for k in
                    ("pmid", "file", "title", "journal", "year", "study_type",
                     "sample_size", "species", "modality", "topics", "clinical_takeaway_ko")}
                   for p in papers],
    }
    with open(INPUT, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(len(papers))


def fallback():
    data = _load(INPUT, None)
    if not data or os.path.exists(data["output_path"]):
        return
    os.makedirs(DIGEST_DIR, exist_ok=True)
    lines = [f"# 주간 논문 다이제스트 {data['date']}", "",
             f"이번 주 새 논문 {data['count']}편", "", "## 전체 목록", ""]
    for p in data["papers"]:
        meta = ", ".join(x for x in (p["study_type"], f"n={p['sample_size']}" if p["sample_size"] else "") if x)
        lines.append(f"- [[papers/{p['file']}|{p['title']}]] ({meta})")
        if p["clinical_takeaway_ko"]:
            lines.append(f"  - {p['clinical_takeaway_ko']}")
    with open(data["output_path"], "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print("기본 목록으로 다이제스트 작성")


def issue(site_url):
    data = _load(INPUT, None)
    if not data or not os.path.exists(data["output_path"]):
        return
    by_file = {p.get("file"): p for p in _load(PAPERS_JSON, [])}
    topic_titles = {t["slug"]: t["title"] for t in _load(TOPICS_JSON, [])}
    with open(data["output_path"], "r", encoding="utf-8") as f:
        text = f.read()

    def link(m):
        target, alias = m.group(1), m.group(2)
        kind, _, name = target.rpartition("/")
        if kind.endswith("papers") and name in by_file:
            p = by_file[name]
            return f"[{alias or p['title']}]({p['url']})"
        if kind.endswith("topics"):
            return alias or topic_titles.get(name, name)
        return alias or name

    text = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", link, text)
    text = re.sub(r"^#\s+.*\n", "", text, count=1)
    header = f"📚 [아카이브 웹페이지에서 보기]({site_url})\n\n" if site_url else ""
    with open(ISSUE_BODY, "w", encoding="utf-8") as f:
        f.write(header + text.strip() + "\n")
    with open(ISSUE_TITLE, "w", encoding="utf-8") as f:
        f.write(f"주간 논문 다이제스트 {data['date']} · 새 논문 {data['count']}편")


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--snapshot" in args:
        snapshot()
    elif "--prepare" in args:
        prepare()
    elif "--fallback" in args:
        fallback()
    elif "--issue" in args:
        i = args.index("--issue")
        issue(args[i + 1] if i + 1 < len(args) else "")
