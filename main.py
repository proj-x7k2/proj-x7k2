# -----------------------------------------------------------------------
# main.py
#
# 이 파일 하나만 실행하면 전체 과정이 순서대로 진행됩니다:
#   1) fetch_papers.py 실행 → 새 논문 찾기
#   2) summarize.py 실행 → 찾은 논문 요약하기
#
# 터미널에서 아래처럼 실행하세요:
#   python main.py
# -----------------------------------------------------------------------

from fetch_papers import fetch_new_papers
from summarize import summarize_new_papers


def main():
    print("=" * 50)
    print("1단계: 새 논문 검색")
    print("=" * 50)
    papers = fetch_new_papers()

    if not papers:
        print("\n새로운 논문이 없어 여기서 종료합니다.")
        return

    print("\n" + "=" * 50)
    print("2단계: 논문 요약 생성")
    print("=" * 50)
    summarize_new_papers()


if __name__ == "__main__":
    main()
