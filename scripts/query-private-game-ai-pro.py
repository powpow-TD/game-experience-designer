#!/usr/bin/env python3
"""Search a locally installed, gitignored Game AI Pro corpus without publishing it."""
from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1] / "private_sources" / "game-ai-pro"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="literal phrase or regular expression")
    parser.add_argument("--regex", action="store_true", help="interpret query as a regular expression")
    parser.add_argument("--context", type=int, default=450, help="characters around each match")
    parser.add_argument("--limit", type=int, default=8, help="maximum matches")
    args = parser.parse_args()
    corpus = ROOT / "full_text.txt"
    if not corpus.is_file():
        raise SystemExit(f"Private corpus not installed: {corpus}")
    text = corpus.read_text(encoding="utf-8", errors="replace")
    pattern = args.query if args.regex else re.escape(args.query)
    matches = list(re.finditer(pattern, text, re.IGNORECASE))[: args.limit]
    if not matches:
        print("No matches.")
        return
    for number, match in enumerate(matches, 1):
        start = max(0, match.start() - args.context)
        end = min(len(text), match.end() + args.context)
        print(f"\n===== MATCH {number} =====\n{text[start:end].strip()}\n")


if __name__ == "__main__":
    main()
