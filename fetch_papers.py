# -----------------------------------------------------------------------
# fetch_papers.py
#
# 이 파일이 하는 일 (초보자를 위한 설명):
#   1. PubMed(의학/수의학 논문 검색 사이트)에 "이런 키워드가 들어간
#      논문 있어?"라고 물어봅니다 (esearch).
#   2. 검색된 논문들의 자세한 정보(제목, 초록, 저자, 저널명, 날짜)를
#      받아옵니다 (efetch).
#   3. 이미 예전에 가져온 논문은 건너뛰고, "새로운" 논문만
#      data/raw_papers.json 파일에 저장합니다.
#
# PubMed API는 무료이며 별도 키(key) 없이도 사용할 수 있습니다.
# -----------------------------------------------------------------------

import requests
import xml.etree.ElementTree as ET
import json
import os
import time
from datetime import datetime, timedelta

import config

# PubMed API의 기본 주소 (이 사이트에 요청을 보냅니다)
BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

# 이미 처리한 논문의 PMID(PubMed 고유 번호)를 기록해두는 파일
SEEN_IDS_PATH = os.path.join(config.DATA_DIR, "seen_ids.json")
RAW_PAPERS_PATH = os.path.join(config.DATA_DIR, "raw_papers.json")


def load_seen_ids():
    """예전에 이미 가져온 논문 번호 목록을 불러옵니다."""
    if not os.path.exists(SEEN_IDS_PATH):
        return set()
    with open(SEEN_IDS_PATH, "r", encoding="utf-8") as f:
        return set(json.load(f))


def save_seen_ids(seen_ids):
    """이번에 처리한 논문 번호까지 포함해서 저장해둡니다."""
    os.makedirs(config.DATA_DIR, exist_ok=True)
    with open(SEEN_IDS_PATH, "w", encoding="utf-8") as f:
        json.dump(sorted(seen_ids), f, ensure_ascii=False, indent=2)


def build_query():
    """
    config.py에 적힌 키워드를 PubMed가 이해할 수 있는 검색어 형태로 조립합니다.

    조건:
    - (제목/초록에 KEYWORDS 중 하나가 포함되거나, FULL_COVERAGE_JOURNALS에
      있는 저널에 실린 논문) 이면서
    - EXCLUDE_SPECIES에 있는 단어가 제목/초록에 하나도 없어야 함
      (말/소/돼지 등 대동물·산업동물 논문을 걸러내기 위함)
    """
    keyword_part = " OR ".join(f'"{k}"[Title/Abstract]' for k in config.KEYWORDS)
    date_query = f'("last {config.DAYS_BACK} days"[PDat])'

    topic_query = f"({keyword_part})"

    if config.FULL_COVERAGE_JOURNALS:
        journal_part = " OR ".join(
            f'"{j}"[Journal]' for j in config.FULL_COVERAGE_JOURNALS
        )
        topic_query = f"(({keyword_part}) OR ({journal_part}))"

    query = f"{topic_query} AND {date_query}"

    if config.EXCLUDE_SPECIES:
        exclude_part = " OR ".join(
            f'"{s}"[Title/Abstract]' for s in config.EXCLUDE_SPECIES
        )
        query = f"{query} NOT ({exclude_part})"

    return query


def search_pmids(query):
    """
    1단계: 검색어에 맞는 논문들의 PMID(고유 번호) 목록을 받아옵니다.

    PubMed는 한 번 요청에 최대 100개 정도까지만 돌려주기 때문에, 결과가
    그보다 많으면 페이지를 넘겨가며(retstart를 늘려가며) 계속 요청해서
    config.MAX_RESULTS에 도달하거나 더 이상 결과가 없을 때까지 전부 모읍니다.
    (예전 버전은 첫 페이지만 가져오고 끝내서, 검색 결과가 30편을 넘으면
    나머지는 조용히 누락됐습니다 — 이제는 안 그렇습니다.)
    """
    page_size = 100
    all_pmids = []
    retstart = 0

    while len(all_pmids) < config.MAX_RESULTS:
        params = {
            "db": "pubmed",
            "term": query,
            "retmax": min(page_size, config.MAX_RESULTS - len(all_pmids)),
            "retstart": retstart,
            "retmode": "json",
            "sort": "pub_date",
        }
        response = requests.get(f"{BASE_URL}/esearch.fcgi", params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
        page_ids = data.get("esearchresult", {}).get("idlist", [])

        all_pmids.extend(page_ids)

        if len(page_ids) < page_size:
            break  # 마지막 페이지까지 다 가져온 것

        retstart += page_size
        time.sleep(0.4)  # PubMed 서버에 너무 빠르게 연속 요청하지 않도록

    return all_pmids


def fetch_details(pmids):
    """2단계: PMID 목록을 가지고 각 논문의 제목/초록/저자 등 상세 정보를 받아옵니다."""
    if not pmids:
        return []

    params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "xml",
    }
    response = requests.get(f"{BASE_URL}/efetch.fcgi", params=params, timeout=30)
    response.raise_for_status()

    root = ET.fromstring(response.text)
    papers = []

    for article in root.findall(".//PubmedArticle"):
        papers.append(_parse_article(article))

    return papers


def _text_or_empty(element, path):
    """XML에서 특정 값을 안전하게 꺼내는 도우미 함수 (값이 없으면 빈 문자열)."""
    found = element.find(path)
    return found.text if found is not None and found.text else ""


def _parse_article(article):
    """PubMed가 돌려주는 XML 한 편 분량을 우리가 쓰기 쉬운 딕셔너리로 변환합니다."""
    pmid = _text_or_empty(article, ".//PMID")
    title = _text_or_empty(article, ".//ArticleTitle")
    journal = _text_or_empty(article, ".//Journal/Title")

    # 초록은 여러 문단(AbstractText)으로 나뉘어 있을 수 있어 모두 이어붙입니다.
    abstract_parts = [
        el.text for el in article.findall(".//Abstract/AbstractText") if el.text
    ]
    abstract = " ".join(abstract_parts)

    authors = []
    for author in article.findall(".//AuthorList/Author"):
        last = _text_or_empty(author, "LastName")
        fore = _text_or_empty(author, "ForeName")
        if last:
            authors.append(f"{fore} {last}".strip())

    year = _text_or_empty(article, ".//PubDate/Year")
    doi = ""
    for id_el in article.findall(".//ArticleIdList/ArticleId"):
        if id_el.get("IdType") == "doi":
            doi = id_el.text

    return {
        "pmid": pmid,
        "title": title,
        "journal": journal,
        "abstract": abstract,
        "authors": authors,
        "year": year,
        "doi": doi,
        "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
    }


def fetch_new_papers():
    """
    이 스크립트의 메인 기능입니다.
    새로운 논문만 골라서 data/raw_papers.json 에 저장하고,
    몇 편을 새로 찾았는지 알려줍니다.
    """
    print("PubMed에서 최근 논문을 검색하는 중...")
    query = build_query()
    pmids = search_pmids(query)
    print(f"검색된 논문 수: {len(pmids)}편")

    seen_ids = load_seen_ids()
    new_pmids = [pid for pid in pmids if pid not in seen_ids]

    if not new_pmids:
        print("새로운 논문이 없습니다. (이미 다 처리된 논문들입니다)")
        # 자동화 스크립트가 "이번엔 새 논문 없음"을 파일만 보고도 알 수 있도록
        # 빈 목록으로 덮어써 둡니다 (지난 실행 결과가 남아있지 않도록).
        os.makedirs(config.DATA_DIR, exist_ok=True)
        with open(RAW_PAPERS_PATH, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=2)
        return []

    print(f"새로 발견된 논문: {len(new_pmids)}편. 상세 정보를 가져오는 중...")
    # PubMed 서버에 너무 빠르게 요청하지 않도록 잠깐 쉬어줍니다.
    time.sleep(0.5)
    papers = fetch_details(new_pmids)

    os.makedirs(config.DATA_DIR, exist_ok=True)
    with open(RAW_PAPERS_PATH, "w", encoding="utf-8") as f:
        json.dump(papers, f, ensure_ascii=False, indent=2)

    seen_ids.update(new_pmids)
    save_seen_ids(seen_ids)

    print(f"완료: {RAW_PAPERS_PATH} 에 {len(papers)}편 저장했습니다.")
    return papers


if __name__ == "__main__":
    fetch_new_papers()
