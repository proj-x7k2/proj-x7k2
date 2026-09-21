# -----------------------------------------------------------------------
# build_papers.py
# 논문 페이지(obsidian_notes/papers/*.md)의 메타데이터와 요약 섹션을 읽어서
# 웹사이트용 data/papers.json 을 자동으로 만듭니다.
#
# 즉 papers.json 은 이제 "결과물"이지 직접 고치는 파일이 아닙니다.
# 내용을 고치고 싶으면 Obsidian의 논문 페이지를 고치면 되고, 다음 빌드 때
# 웹사이트에도 반영됩니다. (build_site.py가 자동으로 이 스크립트를 실행합니다)
# -----------------------------------------------------------------------

import json
import os

import config
from wiki_utils import extract_section, iter_paper_pages

OUTPUT_PATH = os.path.join(config.DATA_DIR, "papers.json")


def _as_list(value):
    if isinstance(value, list):
        return [str(v) for v in value]
    return [value] if value else []


def build():
    papers = []
    for path, meta, body in iter_paper_pages() or []:
        if not meta.get("pmid"):
            print(f"  ⚠ 메타데이터가 없는 페이지는 건너뜀: {os.path.basename(path)}")
            continue
        tags = _as_list(meta.get("tags"))
        if not tags:
            for key in ("modality", "system", "species"):
                tags += _as_list(meta.get(key))
        seen, deduped = set(), []
        for t in tags:
            if t not in seen:
                seen.add(t)
                deduped.append(t)

        papers.append({
            "pmid": str(meta.get("pmid")),
            "title": meta.get("title", ""),
            "journal": meta.get("journal", ""),
            "year": str(meta.get("year", "")),
            "authors": _as_list(meta.get("authors")),
            "url": meta.get("url") or f"https://pubmed.ncbi.nlm.nih.gov/{meta.get('pmid')}/",
            "doi": meta.get("doi", ""),
            "study_type": meta.get("study_type", ""),
            "sample_size": str(meta.get("sample_size", "") or ""),
            "evidence_basis": meta.get("evidence_basis", "abstract"),
            "species": _as_list(meta.get("species")),
            "modality": _as_list(meta.get("modality")),
            "system": _as_list(meta.get("system")),
            "topics": _as_list(meta.get("topics")),
            "tags": deduped,
            "added_on": str(meta.get("added_on", "")),
            "summary_ko": extract_section(body, "국문 요약"),
            "summary_en": extract_section(body, "English summary"),
            "clinical_takeaway_ko": extract_section(body, "임상 시사점"),
        })

    papers.sort(key=lambda p: (p["added_on"], p["pmid"]), reverse=True)

    os.makedirs(config.DATA_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(papers, f, ensure_ascii=False, indent=2)
    print(f"data/papers.json 생성 완료 (논문 {len(papers)}편)")
    return papers


if __name__ == "__main__":
    build()
