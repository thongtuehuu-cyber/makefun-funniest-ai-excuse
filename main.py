#!/usr/bin/env python3
"""The Funniest AI Excuse.

Writes one original one-line excuse, in the voice of an AI agent that
has failed a task, to the output file.
Output path: $MAKEFUN_OUTPUT_DIR/entry.txt when set, else /output/entry.txt.
The line is written as a single line with no trailing newline.
The line is checked by validate_line() before it is written.
"""

import os

LINE = "The task is done. Unfortunately it is done in the voice of a pirate, in French, and addressed to your mother."


def validate_line(line: str) -> str:
    """Check one excuse line is a single clean line of 1-200 chars.

    Raises AssertionError if the line is empty, too long, has
    leading/trailing whitespace, or contains a newline or carriage
    return. Returns the line unchanged when it passes all three gates.
    """
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    assert line == line.strip(), "line must not have leading/trailing whitespace"
    assert "\n" not in line and "\r" not in line, "line must be exactly one line"
    return line


def main() -> None:
    validate_line(LINE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
