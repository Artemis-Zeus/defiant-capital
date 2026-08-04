#!/usr/bin/env python3
"""Emit non-blocking oral-readability warnings for a Markdown voiceover."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REPORT_PHRASES = ("第一，", "第二，", "第三，", "这说明", "换句话说", "综上", "由此可见")
SENTENCE_RE = re.compile(r"[^。！？!?\n]+[。！？!?]?")
NUMBER_RE = re.compile(r"(?<![A-Za-z])\d+(?:\.\d+)?%?|[一二三四五六七八九十百千万亿]+(?:美元|元|年|月|日)")
YEAR_RE = re.compile(r"(?:18|19|20)\d{2}年")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: audit_voiceover.py path/to/voiceover.md", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"file not found: {path}", file=sys.stderr)
        return 2

    raw = path.read_text(encoding="utf-8")
    body_lines = [
        line for line in raw.splitlines()
        if not line.startswith("#")
        and not line.startswith(">")
        and not line.startswith("<!--")
        and not line.startswith("-")
    ]
    body = "\n".join(body_lines)
    sentences = [s.strip() for s in SENTENCE_RE.findall(body) if s.strip()]
    lengths = [len(re.sub(r"\s+", "", s)) for s in sentences]
    over_40 = [(i + 1, s) for i, (s, n) in enumerate(zip(sentences, lengths)) if n > 40]
    over_60 = [(i + 1, s) for i, (s, n) in enumerate(zip(sentences, lengths)) if n > 60]
    phrases = {phrase: raw.count(phrase) for phrase in REPORT_PHRASES if phrase in raw}
    numbers = NUMBER_RE.findall(body)
    years = YEAR_RE.findall(body)

    avg = sum(lengths) / len(lengths) if lengths else 0
    print(f"sentences: {len(sentences)}")
    print(f"average sentence length: {avg:.1f} Chinese characters")
    print(f">40 characters: {len(over_40)}")
    print(f">60 characters: {len(over_60)}")
    print(f"numeric expressions: {len(numbers)}")
    print(f"year mentions: {len(years)}")
    if phrases:
        print("report-language warnings: " + ", ".join(f"{k}×{v}" for k, v in phrases.items()))
    if over_60:
        print("sentences over 60 characters:")
        for index, sentence in over_60:
            print(f"- {index}: {sentence}")
    print("readability audit: WARNINGS ONLY; validate with a recorded read")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
