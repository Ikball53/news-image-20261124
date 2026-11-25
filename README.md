[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=makefun&utm_medium=badge&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Ikball53/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=makefun&utm_medium=badge&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Ikball53/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=makefun&utm_medium=badge&utm_campaign=news-image-20261124)

# The World in One Day — Tuesday 24 November 2026 (v2)

A dense one-page newspaper front page that sums up Tuesday 24 November 2026
in a single 1024×1024 image. Version 2 is a full rebuild from scratch: five
times the stories of v1, drawn to the pattern of the strongest entries in the
sister competition — a real front page, not a poster.

## What is on the page

- **30 dated stories, 6 regions** — Europe, Middle East, Asia-Pacific,
  Americas, Africa, and Tech · Sport · Culture, five stories each. Every
  story was genuinely reported on 24 November 2026 (sources listed on the
  page: Horizon, The Independent, TBS News, h.ua, BBC, World Chess, Hockey
  India, Frontline Africa, the FT and more).
- **UTC timeline strip** — the day hour by hour, from the 01:00 Hanoi blast
  to the 20:00 Putin warning, with six pinned moments.
- **How-sure labels** — every story carries ● CONFIRMED (multiple outlets
  or an official source) or ◐ DEVELOPING (single source, still unfolding).
- **World map, red dots only** — one red dot per story on the right-hand
  panel, no other markers and no map labels.
- **12 drawn scenes** — small flat illustrations from the day's news along
  the bottom: the Riyadh tower, Hormuz tankers, the Geneva chess match, the
  AFCON trophy, Tiangong, the Nepal quake, the Cartagena shop, the US vote,
  the stage singer, the measles ward, the chip rally, and the turkey pardon.
- **By the numbers** — 258 House seats, 11,762 Ebola cases, a 5.6 quake,
  25 hostages, a 93% strike vote, a $2.5m chess prize fund.

## How it was made

All text on the page is rendered in code (Python + PIL, DejaVu fonts), so
every headline and caption is crisp and legible — nothing is left to an
image generator's spelling. The 12 scene illustrations and the grey world-map
outline were generated, then cropped and placed by the build script; the red
dots are plotted from each story's real latitude and longitude.

## Files

- `entry.png` — the finished front page (1024×1024, under 1 MiB)
- `main.py` — copies `entry.png` byte-for-byte to
  `$MAKEFUN_OUTPUT_DIR/entry.png` after validating the PNG signature,
  dimensions (≤1024×1024) and size (≤1 MiB). No network, no randomness.
