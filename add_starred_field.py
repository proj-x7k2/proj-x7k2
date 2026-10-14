# -----------------------------------------------------------------------
# add_starred_field.py — 1회용. 기존 논문 페이지에 "starred: false" 속성을 추가해서
# Obsidian에서 체크박스로 "나중에 볼 논문"을 표시할 수 있게 합니다.
#   python3 add_starred_field.py
# -----------------------------------------------------------------------
import os
import re

import config

papers_dir = os.path.join(config.OBSIDIAN_DIR, "papers")
changed = 0
for name in sorted(os.listdir(papers_dir)):
    if not name.endswith(".md"):
        continue
    path = os.path.join(papers_dir, name)
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m or re.search(r"^starred\s*:", m.group(1), re.MULTILINE):
        continue
    text = text[:m.end(1)] + "\nstarred: false" + text[m.end(1):]
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    changed += 1
print(f"{changed}개 논문 페이지에 starred 속성을 추가했습니다.")
