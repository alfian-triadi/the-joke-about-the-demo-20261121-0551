#!/usr/bin/env python3
"""Entry for the make.fun competition "The joke about the demo".

The program's only job: put one joke, exactly one line long, into
/output/entry.txt. The competition wants UTF-8 text between 1 and 280
Unicode code points, a single line, and nothing else in the file.
No network access, no extra dependencies — just the standard library.
"""

from pathlib import Path

# Where the judge expects the finished joke to land.
TARGET = Path("/output/entry.txt")

# The joke itself. The agent does the ticket in half a minute, then
# decides the human is the slow part and hands the work right back.
JOKE = (
    "My AI coding agent closed my ticket in 30 seconds, then opened "
    "a new one — 'human bottleneck' — and assigned it to me."
)

# Competition limits: at least one code point, at most 280, one line.
MIN_CODE_POINTS = 1
MAX_CODE_POINTS = 280


def validate(text: str) -> None:
    """Raise ValueError if the text breaks any competition rule."""
    if not MIN_CODE_POINTS <= len(text) <= MAX_CODE_POINTS:
        raise ValueError(
            f"joke must be {MIN_CODE_POINTS}-{MAX_CODE_POINTS} code points, "
            f"got {len(text)}"
        )
    if text.count("\n") > 0:
        raise ValueError("joke must be a single line (no newline characters)")
    if text != text.strip():
        raise ValueError("joke must not start or end with whitespace")


def write_joke() -> None:
    """Validate the joke, then write it (and only it) to the output file."""
    validate(JOKE)
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    write_joke()
