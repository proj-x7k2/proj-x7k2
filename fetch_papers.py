# -----------------------------------------------------------------------
# fetch_papers.py  (v2)
#
# 이 파일이 하는 일:
#   1. PubMed에서 config.py 조건에 맞는 논문을 "최근 등록된 날짜" 기준으로 찾습니다.
#   2. 아직 처리하지 않은 논문만 골라 상세 정보(초록, 논문 유형, MeSH 등)를 받습니다.
#   3. 원자료를 raw/pubmed/{pmid}.json 에 영구 보관하고 (절대 덮어쓰지 않음),
#      이번 실행분 목록을 data/raw_papers.json 에 저장합니다.
#
# "처리 완료" 표시는 여기서 하지 않습니다. Claude가 위키에 실제로 반영했거나
# 의도적으로 건너뛴 것이 확인된 뒤에(--reconcile) 표시합니다. 그래서 중간에
# 사용량 한도나 오류로 멈춰도, 남은 논문은 다음 실행 때 다시 처리됩니다.
#
# 사용법:
#   python3 fetch_papers.py              새 논문 수집 (run_weekly.sh가 자동 실행)
#   python3 fetch_papers.py --dry-run    저장 없이 검색 결과 수만 확인 (조건 테스트용)
#   python3 fetch_papers.py --reconcile  위키 반영이 끝난 논문을 "처리 완료"로 표시
#   python3 fetch_papers.py --backfill   기존 위키 논문들의 원자료를 raw/에 채워넣기 (1회용)
# -----------------------------------------------------------------------

import json
import os
import sys
import time
import xml.etree.ElementTree as ET

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

import config
from wiki_utils import iter_paper_pages, processed_pmids

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
SEEN_IDS_PATH = os.path.join(config.DATA_DIR, "seen_ids.json")
RAW_PAPERS_PATH = os.path.join(config.DATA_DIR, "raw_papers.json")
RAW_PUBMED_DIR = os.path.join(config.RAW_DIR, "pubmed")


def _build_session():
    """PubMed가 느리거나 일시적으로 실패할 때 2·4·8초 간격으로 최대 3번 재시도."""
    session = requests.Session()
    retry = Retry(total=3, backoff_factor=2,
                  status_forcelist=[429, 500, 502, 503, 504],
                  allowed_methods=["GET", "POST"])
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    return session


SESSION = _build_session()


# ── 처리 기록 ───────────────────────────────────────────────────────────

def load_seen_ids():
    if not os.path.exists(SEEN_IDS_PATH):
        return set()
    with open(SEEN_IDS_PATH, "r", encoding="utf-8") as f:
        return set(str(x) for x in json.load(f))


def save_seen_ids(seen_ids):
    os.makedirs(config.DATA_DIR, exist_ok=True)
    with open(SEEN_IDS_PATH, "w", encoding="utf-8") as f:
        json.dump(sorted(seen_ids), f, ensure_ascii=False, indent=2)


# ── 검색 ───────────────────────────────────────────────────────────────

def build_query():
    imaging = " OR ".join(config.IMAGING_TERMS)
    if config.FULL_COVERAGE_JOURNALS:
        imaging += " OR " + " OR ".join(f'"{j}"[Journal]' for j in config.FULL_COVERAGE_JOURNALS)
    species = " OR ".join(config.SPECIES_TERMS)
    vet = " OR ".join(config.VET_CONTEXT_TERMS + [f'"{j}"[Journal]' for j in config.VET_JOURNALS])
    return f"({imaging}) AND ({species}) AND ({vet})"


def search_pmids(query):
    """조건에 맞는 PMID를 전부 받아옵니다 (번호만이라 가볍습니다)."""
    page_size = 1000
    all_ids, retstart = [], 0
    while True:
        params = {
            "db": "pubmed", "term": query,
            "datetype": "edat", "reldate": config.DAYS_BACK,   # PubMed 등록일 기준
            "retmax": page_size, "retstart": retstart,
            "retmode": "json", "sort": "pub_date",
        }
        response = SESSION.post(f"{BASE_URL}/esearch.fcgi", data=params, timeout=60)
        response.raise_for_status()
        result = response.json().get("esearchresult", {})
        ids = result.get("idlist", [])
        all_ids.extend(ids)
        total = int(result.get("count", 0))
        retstart += page_size
        if not ids or retstart >= total:
            break
        time.sleep(0.4)
    return all_ids


# ── 상세 정보 ──────────────────────────────────────────────────────────

def _text(element, path):
    found = element.find(path)
    return "".join(found.itertext()).strip() if found is not None else ""


def _parse_article(article):
    pmid = _text(article, ".//PMID")

    abstract_parts = []
    for el in article.findall(".//Abstract/AbstractText"):
        label = el.get("Label")
        content = "".join(el.itertext()).strip()
        if content:
            abstract_parts.append(f"{label}: {content}" if label else content)

    authors = []
    for author in article.findall(".//AuthorList/Author"):
        last, fore = _text(author, "LastName"), _text(author, "ForeName")
        if last:
            authors.append(f"{fore} {last}".strip())

    year = _text(article, ".//JournalIssue/PubDate/Year") or _text(article, ".//ArticleDate/Year")
    doi = ""
    for id_el in article.findall(".//ArticleIdList/ArticleId"):
        if id_el.get("IdType") == "doi":
            doi = (id_el.text or "").strip()

    return {
        "pmid": pmid,
        "title": _text(article, ".//ArticleTitle"),
        "journal": _text(article, ".//Journal/Title"),
        "year": year,
        "authors": authors,
        "doi": doi,
        "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
        "abstract": "\n\n".join(abstract_parts),
        # 연구 유형 판단에 도움이 되는 PubMed 공식 분류 (예: Review, Case Reports)
        "publication_types": [pt.text for pt in article.findall(".//PublicationTypeList/PublicationType") if pt.text],
        "mesh_terms": [d.text for d in article.findall(".//MeshHeadingList/MeshHeading/DescriptorName") if d.text],
        "keywords": [k.text for k in article.findall(".//KeywordList/Keyword") if k.text],
        "fetched_on": time.strftime("%Y-%m-%d"),
    }


def fetch_details(pmids):
    papers = []
    for i in range(0, len(pmids), 100):
        chunk = pmids[i:i + 100]
        response = SESSION.post(f"{BASE_URL}/efetch.fcgi",
                                data={"db": "pubmed", "id": ",".join(chunk), "retmode": "xml"},
                                timeout=60)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        papers.extend(_parse_article(a) for a in root.findall(".//PubmedArticle"))
        time.sleep(0.4)
    return papers


def archive_raw(papers):
    """원자료 층: 논문마다 raw/pubmed/{pmid}.json 을 한 번만 저장 (덮어쓰지 않음)."""
    os.makedirs(RAW_PUBMED_DIR, exist_ok=True)
    for p in papers:
        path = os.path.join(RAW_PUBMED_DIR, f"{p['pmid']}.json")
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                json.dump(p, f, ensure_ascii=False, indent=2)


def write_batch(papers):
    os.makedirs(config.DATA_DIR, exist_ok=True)
    with open(RAW_PAPERS_PATH, "w", encoding="utf-8") as f:
        json.dump(papers, f, ensure_ascii=False, indent=2)


# ── 동작 모드 ──────────────────────────────────────────────────────────

def fetch_new_papers(dry_run=False):
    print(f"PubMed 검색 중 (최근 {config.DAYS_BACK}일 등록분)...")
    pmids = search_pmids(build_query())
    print(f"검색된 논문 수: {len(pmids)}편")

    done = load_seen_ids() | processed_pmids()
    new_pmids = [p for p in pmids if p not in done]
    print(f"아직 처리 안 된 논문: {len(new_pmids)}편")

    if dry_run:
        print("(--dry-run: 저장하지 않고 종료)")
        return []

    if len(new_pmids) > config.MAX_RESULTS:
        print(f"이번 실행은 {config.MAX_RESULTS}편만 넘기고, 나머지 "
              f"{len(new_pmids) - config.MAX_RESULTS}편은 다음 실행 때 처리합니다.")
        new_pmids = new_pmids[:config.MAX_RESULTS]

    if not new_pmids:
        write_batch([])
        print("새로운 논문이 없습니다.")
        return []

    papers = fetch_details(new_pmids)
    archive_raw(papers)
    write_batch(papers)
    print(f"완료: {len(papers)}편을 raw/pubmed/ 에 보관하고 이번 처리 목록에 올렸습니다.")
    return papers


def reconcile():
    """이번 처리 목록 중 위키에 반영됐거나 건너뛴 것이 확인된 논문만 '처리 완료'로 표시."""
    if not os.path.exists(RAW_PAPERS_PATH):
        return
    with open(RAW_PAPERS_PATH, "r", encoding="utf-8") as f:
        batch = [str(p["pmid"]) for p in json.load(f)]
    done = processed_pmids()
    seen = load_seen_ids()
    finished = [p for p in batch if p in done]
    unfinished = [p for p in batch if p not in done]
    seen.update(finished)
    save_seen_ids(seen)
    print(f"처리 확인: {len(finished)}편 완료 표시"
          + (f", {len(unfinished)}편은 미처리로 남겨 다음 실행 때 재시도" if unfinished else ""))


def backfill():
    """기존 위키 논문들의 원자료를 raw/pubmed/ 에 채워넣습니다 (v2 이전 1회용)."""
    pmids = set()
    for _, meta, _ in iter_paper_pages() or []:
        if meta.get("pmid"):
            pmids.add(str(meta["pmid"]))
    papers_json = os.path.join(config.DATA_DIR, "papers.json")
    if os.path.exists(papers_json):
        with open(papers_json, "r", encoding="utf-8") as f:
            pmids.update(str(p["pmid"]) for p in json.load(f) if p.get("pmid"))
    missing = [p for p in sorted(pmids)
               if not os.path.exists(os.path.join(RAW_PUBMED_DIR, f"{p}.json"))]
    if not missing:
        print("채워넣을 원자료가 없습니다.")
        return
    papers = fetch_details(missing)
    archive_raw(papers)
    print(f"원자료 {len(papers)}편을 raw/pubmed/ 에 보관했습니다.")


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--reconcile" in args:
        reconcile()
    elif "--backfill" in args:
        backfill()
    else:
        fetch_new_papers(dry_run="--dry-run" in args)
