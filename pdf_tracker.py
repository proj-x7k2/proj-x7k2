# -----------------------------------------------------------------------
# pdf_tracker.py — raw/pdf/ 에 새로 넣은 PDF를 추적합니다 (run_weekly.sh가 사용)
#   --pending-count  아직 위키에 반영 안 된 PDF 개수 출력
#   --mark-done      지금 있는 PDF들을 "반영 완료"로 기록
# -----------------------------------------------------------------------
import json
import os
import sys

import config

PDF_DIR = os.path.join(config.RAW_DIR, "pdf")
DONE_PATH = os.path.join(config.DATA_DIR, "pdf_done.json")


def _current():
    if not os.path.isdir(PDF_DIR):
        return []
    return sorted(f for f in os.listdir(PDF_DIR) if f.lower().endswith(".pdf"))


def _done():
    if not os.path.exists(DONE_PATH):
        return set()
    with open(DONE_PATH, "r", encoding="utf-8") as f:
        return set(json.load(f))


if __name__ == "__main__":
    if "--mark-done" in sys.argv:
        os.makedirs(config.DATA_DIR, exist_ok=True)
        merged = sorted(_done() | set(_current()))   # 파일을 열기 전에 먼저 계산
        with open(DONE_PATH, "w", encoding="utf-8") as f:
            json.dump(merged, f, ensure_ascii=False, indent=2)
    else:
        print(len([p for p in _current() if p not in _done()]))
