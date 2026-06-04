#!/usr/bin/env python3
"""Generate REPO_INDEX.md from the repository topic folders."""
from __future__ import annotations
from pathlib import Path
import re
ROOT = Path(__file__).resolve().parents[1]
TOPICS = [
("arrays-hashing","Arrays & Hashing"),("two-pointers","Two Pointers"),("stack","Stack"),("binary-search","Binary Search"),("sliding-window","Sliding Window"),("linked-list","Linked List"),("trees","Trees"),("tries","Tries"),("heap-priority-queue","Heap / Priority Queue"),("backtracking","Backtracking"),("graphs","Graphs"),("advanced-graphs","Advanced Graphs"),("1d-dp","1-D Dynamic Programming"),("2d-dp","2-D Dynamic Programming"),("greedy","Greedy"),("intervals","Intervals"),("bit-manipulation","Bit Manipulation"),("math-geometry","Math & Geometry")]

def count(path: Path, pattern: str) -> int:
    return len(re.findall(pattern, path.read_text(encoding="utf-8"), flags=re.MULTILINE))

def main() -> int:
    rows = []
    total_problems = 0
    total_patterns = 0
    for slug, name in TOPICS:
        folder = ROOT / slug
        easy = count(folder / "easy.md", r"^## \d+\. ")
        medium = count(folder / "medium.md", r"^## \d+\. ")
        hard = count(folder / "hard.md", r"^## \d+\. ")
        patterns = count(folder / "PATTERNS.md", r"^## Pattern: ")
        subtotal = easy + medium + hard
        total_problems += subtotal
        total_patterns += patterns
        rows.append(f"| [{name}]({slug}/README.md) | {easy} | {medium} | {hard} | {subtotal} | {patterns} |")
    markdown_count = len([p for p in ROOT.rglob("*.md") if ".git" not in p.parts])
    content = f"""# Repository Index

Generated overview of the Data Structures and Algorithms repository.

## Summary

| Metric | Count |
|---|---:|
| Topic folders | {len(TOPICS)} |
| Markdown files | {markdown_count} |
| Curated problem entries | {total_problems} |
| Pattern sections | {total_patterns} |

## Topics

| Topic | Easy | Medium | Hard | Total Problems | Patterns |
|---|---:|---:|---:|---:|---:|
{chr(10).join(rows)}

## Root Documents

- [README.md](README.md)
- [ROADMAP.md](ROADMAP.md)
- [STUDY_PLAN.md](STUDY_PLAN.md)
- [INTERVIEW_GUIDE.md](INTERVIEW_GUIDE.md)

## Validation Tools

- [tools/generate_repo_index.py](tools/generate_repo_index.py)
- [tools/check_links.py](tools/check_links.py)
- [tools/check_markdown_quality.py](tools/check_markdown_quality.py)

---

## Navigation

[Previous](INTERVIEW_GUIDE.md) | [Home](README.md) | [Next](arrays-hashing/README.md)
"""
    (ROOT / "REPO_INDEX.md").write_text(content, encoding="utf-8")
    print(f"Generated REPO_INDEX.md with {total_problems} problems and {total_patterns} patterns.")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
