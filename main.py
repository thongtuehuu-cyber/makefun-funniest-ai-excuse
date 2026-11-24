#!/usr/bin/env python3
"""The Funniest AI Excuse.

Writes one original one-line excuse, in the voice of an AI agent that
has failed a task, to the output file.
Output path: $MAKEFUN_OUTPUT_DIR/entry.txt when set, else /output/entry.txt.
The line is written as a single line with no trailing newline.
"""

import os

LINE = "The task is done. Unfortunately it is done in the voice of a pirate, in French, and addressed to your mother."


def main() -> None:
    # Gate: one line, 1-200 chars, no leading/trailing whitespace.
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    assert LINE == LINE.strip(), "line must not have leading/trailing whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "line must be exactly one line"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
