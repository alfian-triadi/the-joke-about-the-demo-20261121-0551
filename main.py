#!/usr/bin/env python3
"""One-line joke about working beside AI coding agents.

Writes the joke to /output/entry.txt, exactly as the make.fun
competition "The joke about the demo" requires: UTF-8 text of
1-280 characters (Unicode code points), a single line, no network.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

JOKE = (
    "My AI coding agent closed my ticket in 30 seconds, then opened "
    "a new one \u2014 'human bottleneck' \u2014 and assigned it to me."
)

MAX_LEN = 280


def main() -> None:
    assert 1 <= len(JOKE) <= MAX_LEN, "joke must be 1-280 code points"
    assert "\n" not in JOKE, "joke must be a single line"
    assert JOKE == JOKE.strip(), "joke must not have leading/trailing whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
