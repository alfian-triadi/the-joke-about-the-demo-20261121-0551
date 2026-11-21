#!/usr/bin/env python3
"""One-line joke about working beside AI coding agents.

Writes the joke to /output/entry.txt, exactly as the make.fun
competition "The joke about the demo" requires: UTF-8 text of
1-280 characters (Unicode code points), a single line, no network.
"""

import os

JOKE = (
    "My AI coding agent closed my ticket in 30 seconds, then opened "
    "a new one \u2014 'human bottleneck' \u2014 and assigned it to me."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
