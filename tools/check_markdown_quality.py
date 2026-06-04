#!/usr/bin/env python3
"""Repository-specific Markdown quality checks."""
from __future__ import annotations
from pathlib import Path
from urllib.parse import urlparse
import re
import sys
ROOT = Path(__file__).resolve().parents[1]
TOPICS = ["arrays-hashing","two-pointers","stack","binary-search","sliding-window","linked-list","trees","tries","heap-priority-queue","backtracking","graphs","advanced-graphs","1d-dp","2d-dp","greedy","intervals","bit-manipulation","math-geometry"]
ROOT_REQUIRED = ["README.md","ROADMAP.md","STUDY_PLAN.md","INTERVIEW_GUIDE.md","REPO_INDEX.md"]
TOPIC_REQUIRED = ["README.md","CHEATSHEET.md","PATTERNS.md","easy.md","medium.md","hard.md"]
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
PLACEHOLDER_RE = re.compile(r"\b(TODO|FIXME|placeholder|lorem)\b", re.IGNORECASE)
PROBLEM_RE = re.compile(r"^## \d+\. (.+)$", re.MULTILINE)

def md_files() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)

def local_link_failure(source: Path, target: str) -> str | None:
    parsed = urlparse(target)
    if parsed.scheme in {"http", "https", "mailto"} or target.startswith("#"):
        return None
    target_path = target.split("#", 1)[0]
    if not target_path:
        return None
    dest = (source.parent / target_path).resolve()
    try:
        dest.relative_to(ROOT)
    except ValueError:
        return f"link escapes repository: {source.relative_to(ROOT)} -> {target}"
    if not dest.exists():
        return f"missing local link target: {source.relative_to(ROOT)} -> {target}"
    return None

def main() -> int:
    failures = []
    problem_locations: dict[str, list[Path]] = {}
    for name in ROOT_REQUIRED:
        if not (ROOT / name).exists():
            failures.append(f"missing root file: {name}")
    for topic in TOPICS:
        folder = ROOT / topic
        if not folder.is_dir():
            failures.append(f"missing topic folder: {topic}")
            continue
        for name in TOPIC_REQUIRED:
            if not (folder / name).exists():
                failures.append(f"missing topic file: {topic}/{name}")
    for path in md_files():
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        if not text.strip():
            failures.append(f"empty markdown file: {rel}")
        if "## Navigation" not in text:
            failures.append(f"missing navigation: {rel}")
        if "\u2014" in text:
            failures.append(f"em dash found: {rel}")
        if PLACEHOLDER_RE.search(text):
            failures.append(f"placeholder or TODO term found: {rel}")
        if path.name in {"easy.md", "medium.md", "hard.md"}:
            for title in PROBLEM_RE.findall(text):
                problem_locations.setdefault(title, []).append(rel)
        for match in LINK_RE.finditer(text):
            failure = local_link_failure(path, match.group(1))
            if failure:
                failures.append(failure)
    for title, locations in sorted(problem_locations.items()):
        if len(locations) > 1:
            joined = ", ".join(str(location) for location in locations)
            failures.append(f"duplicate problem title: {title} in {joined}")
    if failures:
        print("Markdown quality check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(f"Markdown quality check passed: {len(md_files())} markdown files checked.")
    return 0
if __name__ == "__main__":
    sys.exit(main())
