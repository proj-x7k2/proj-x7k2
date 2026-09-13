# -----------------------------------------------------------------------
# summarize.py
#
# 참고: 이 스크립트는 (B) API 키를 직접 쓰는 수동 방식입니다. 논문마다
# 독립된 노트만 만들고, topics/overview.md 같은 위키 통합은 하지 않습니다.
# 주제별로 통합되는 진짜 위키를 쓰시려면 README 9-6단계의 CLAUDE.md +
# Claude Code 방식(run_weekly.sh)을 쓰세요.
#
# 이 파일이 하는 일 (초보자를 위한 설명):
#   1. fetch_papers.py 가 만들어 둔 data/raw_papers.json (초록 원문)을
#      하나씩 읽습니다.
#   2. 각 논문의 초록을 Claude API에게 보내서
#      "영문 요약 / 국문 요약 / 임상 시사점"을 만들어달라고 요청합니다.
#   3. 결과를 두 곳에 저장합니다.
#        - obsidian_notes/ 폴더 : 마크다운(.md) 노트 (Obsidian 위키용)
#        - data/papers.json     : 웹사이트가 읽어갈 데이터 목록
# -----------------------------------------------------------------------

import json
import os
import re
from datetime import date

import anthropic
from dotenv import load_dotenv

import config

load_dotenv()  # .env 파일에 적어둔 API 키를 불러옵니다.

RAW_PAPERS_PATH = os.path.join(config.DATA_DIR, "raw_papers.json")
PAPERS_JSON_PATH = os.path.join(config.DATA_DIR, "papers.json")

client = anthropic.Anthropic()  # .env의 ANTHROPIC_API_KEY를 자동으로 사용합니다.

# Claude에게 보낼 지시문(프롬프트) 템플릿입니다.
# {title} / {journal} / {abstract} 자리에 실제 논문 정보가 들어갑니다.
PROMPT_TEMPLATE = """당신은 수의영상의학(수의 MRI/CT/초음파) 전문가를 돕는 보조원입니다.
아래 논문 초록을 읽고, 임상 수의사가 빠르게 트렌드를 파악할 수 있도록 요약하세요.

제목: {title}
저널: {journal}
초록: {abstract}

국문 요약을 쓸 때, 의학/해부학/영상의학 전문 용어(질환명, 해부학적 구조,
영상 기법, 약물명 등)는 국문으로 번역하지 말고 영어 원어를 그대로 쓰세요.
조사와 문장 흐름만 자연스럽게 국문으로 연결하면 됩니다.
예 (권장): "이 종양은 T2-weighted 영상에서 hyperintense 신호를 보였다."
예 (지양): "이 종양은 T2 강조 영상에서 고신호강도를 보였다."

다음 JSON 형식으로만 답하세요. 다른 설명 없이 JSON만 출력하세요.
{{
  "summary_en": "3-4문장 영문 요약",
  "summary_ko": "3-4문장 국문 요약 (전문 용어는 영어 원어 유지)",
  "clinical_takeaway_ko": "임상 적용 관점에서의 시사점 1-2문장 (국문, 전문 용어는 영어 원어 유지)",
  "tags": ["관련 키워드 3-5개, 예: MRI, oncology, canine"]
}}
"""


def slugify(text, max_len=60):
    """논문 제목을 파일 이름으로 써도 안전하도록 특수문자를 정리합니다."""
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    text = re.sub(r"[\s]+", "-", text)
    return text[:max_len] if text else "untitled"


def call_claude_for_summary(paper):
    """Claude API에 논문 한 편을 보내고, 구조화된 요약(JSON)을 받아옵니다."""
    prompt = PROMPT_TEMPLATE.format(
        title=paper["title"],
        journal=paper["journal"],
        abstract=paper["abstract"] or "(초록 없음)",
    )

    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=800,
        messages=[{"role": "user", "content": prompt}],
    )

    raw_text = message.content[0].text.strip()

    # 혹시 Claude가 ```json 같은 코드블록으로 감싸서 답하면 벗겨냅니다.
    raw_text = re.sub(r"^```json|```$", "", raw_text, flags=re.MULTILINE).strip()

    try:
        return json.loads(raw_text)
    except json.JSONDecodeError:
        print(f"  ⚠ JSON 파싱 실패, 원본 응답을 그대로 저장합니다: {paper['title'][:40]}...")
        return {
            "summary_en": raw_text,
            "summary_ko": "",
            "clinical_takeaway_ko": "",
            "tags": [],
        }


def write_obsidian_note(paper, summary):
    """Obsidian 위키에 들어갈 마크다운 노트 파일을 만듭니다."""
    os.makedirs(config.OBSIDIAN_DIR, exist_ok=True)

    filename = f"{paper['year']}-{slugify(paper['title'])}.md"
    filepath = os.path.join(config.OBSIDIAN_DIR, filename)

    tags = summary.get("tags", [])
    tags_line = " ".join(f"#{tag.replace(' ', '_')}" for tag in tags)

    content = f"""# {paper['title']}

- **저널**: {paper['journal']} ({paper['year']})
- **저자**: {', '.join(paper['authors'])}
- **PubMed**: {paper['url']}
- **DOI**: {paper.get('doi', '')}

{tags_line}

## 국문 요약
{summary.get('summary_ko', '')}

## English summary
{summary.get('summary_en', '')}

## 임상 시사점
{summary.get('clinical_takeaway_ko', '')}

## 원문 초록
{paper['abstract']}
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return filepath


def append_to_website_data(paper, summary):
    """웹사이트가 읽어갈 data/papers.json 목록 맨 앞에 새 논문을 추가합니다."""
    if os.path.exists(PAPERS_JSON_PATH):
        with open(PAPERS_JSON_PATH, "r", encoding="utf-8") as f:
            all_papers = json.load(f)
    else:
        all_papers = []

    entry = {
        "pmid": paper["pmid"],
        "title": paper["title"],
        "journal": paper["journal"],
        "year": paper["year"],
        "authors": paper["authors"],
        "url": paper["url"],
        "doi": paper.get("doi", ""),
        "summary_en": summary.get("summary_en", ""),
        "summary_ko": summary.get("summary_ko", ""),
        "clinical_takeaway_ko": summary.get("clinical_takeaway_ko", ""),
        "tags": summary.get("tags", []),
        "added_on": date.today().isoformat(),
    }

    all_papers.insert(0, entry)  # 최신 논문이 맨 위로 오도록

    os.makedirs(config.DATA_DIR, exist_ok=True)
    with open(PAPERS_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(all_papers, f, ensure_ascii=False, indent=2)


def summarize_new_papers():
    """이 스크립트의 메인 기능: raw_papers.json에 있는 논문들을 모두 요약합니다."""
    if not os.path.exists(RAW_PAPERS_PATH):
        print("data/raw_papers.json 이 없습니다. 먼저 fetch_papers.py를 실행하세요.")
        return

    with open(RAW_PAPERS_PATH, "r", encoding="utf-8") as f:
        papers = json.load(f)

    if not papers:
        print("요약할 새 논문이 없습니다.")
        return

    print(f"{len(papers)}편의 논문을 요약합니다...")

    for i, paper in enumerate(papers, start=1):
        print(f"[{i}/{len(papers)}] {paper['title'][:60]}...")
        summary = call_claude_for_summary(paper)
        note_path = write_obsidian_note(paper, summary)
        append_to_website_data(paper, summary)
        print(f"  → 저장 완료: {note_path}")

    print("\n모든 논문 요약이 끝났습니다.")
    print(f"- Obsidian 노트: {config.OBSIDIAN_DIR}/ 폴더")
    print(f"- 웹사이트 데이터: {PAPERS_JSON_PATH}")


if __name__ == "__main__":
    summarize_new_papers()
