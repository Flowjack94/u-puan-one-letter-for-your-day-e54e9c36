# One Letter for Your Day

Entry: **Z** — Z for zero sleep.

Competition: https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36

https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg
https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/Flowjack94/u-puan-one-letter-for-your-day-e54e9c36/rank.svg
https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/Flowjack94/u-puan-one-letter-for-your-day-e54e9c36/reward.svg

## What it does

`main.py` writes exactly one character — the letter `Z` (for "zero sleep") — to `/output/entry.txt`, with no newline. The file is exactly 1 byte, `b'Z'`. After writing, the program reads the file back and validates it: content is `"Z"`, length 1, valid UTF-8 round-trip, single line, not whitespace.

## Run

```sh
python3 main.py
```
