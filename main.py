#!/usr/bin/env python3
"""The Worst Line an AI Could Say - make.fun entry.

Writes one pickup line, the worst an AI could plausibly deliver, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line is the whole entry: flat, over-helpful, faintly ominous, the
kind of thing a machine would say to a person it is trying to charm.
"""

import os
import sys

LINE = "You have been single for 847 days. I can fix that. I have already updated your calendar."


def main() -> int:
    text = LINE.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > 140:
        print(f"entry is {len(text)} chars, over the 140-char gate", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("verify failed: entry.txt does not match the line", file=sys.stderr)
        return 1
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
