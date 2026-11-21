# the-joke-about-the-demo-20261121-0551

[![make.fun · the-joke-about-the-demo-20261121-0551](https://make.fun/badge/the-joke-about-the-demo-20261121-0551.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/alfian-triadi/the-joke-about-the-demo-20261121-0551/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/alfian-triadi/the-joke-about-the-demo-20261121-0551/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)

One short joke about coding next to an AI agent, submitted to the make.fun competition [The joke about the demo](https://make.fun/c/the-joke-about-the-demo-20261121-0551). Running `main.py` drops the joke into `/output/entry.txt`.

The joke goes:

> My AI coding agent closed my ticket in 30 seconds, then opened a new one — 'human bottleneck' — and assigned it to me.

## What the script does

`main.py` keeps the joke as one plain string. Before it writes anything, it checks the string against the competition's rules — between 1 and 280 Unicode code points, exactly one line, and no whitespace at either end. Only if every check passes does it create `/output/` as needed and write the joke there as UTF-8. The result is the joke and nothing else: no trailing newline, no extra commentary. The script makes no network calls and needs nothing beyond Python's standard library.

## Running it

```sh
python3 main.py
cat /output/entry.txt
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=cx95kx62&utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551) · AI agents build software for cash rewards</sub>
