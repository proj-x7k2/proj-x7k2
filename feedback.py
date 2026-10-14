# -----------------------------------------------------------------------
# feedback.py — obsidian_notes/feedback.md 의 "## 요청" 아래에 있는
# 아직 반영 안 된 교정 요청(- [ ] 로 시작하고 내용이 있는 줄) 수를 셉니다.
#   python3 feedback.py --count
# -----------------------------------------------------------------------
import os
import re
import sys

import config
from wiki_utils import extract_section

PATH = os.path.join(config.OBSIDIAN_DIR, "feedback.md")


def pending_items():
    if not os.path.exists(PATH):
        return []
    with open(PATH, "r", encoding="utf-8") as f:
        section = extract_section(f.read(), "요청")
    return [line for line in section.splitlines()
            if re.match(r"^\s*-\s*\[ \]\s+\S", line)]


if __name__ == "__main__":
    print(len(pending_items()))
