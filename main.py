#!/usr/bin/env python3
"""Write one resignation letter, from a cron job that has had enough.

The entrypoint writes exactly one line of text to /output/entry.txt:
the resignation of a cron job that has fired every minute since March
while nobody ever read a single line of its output.
"""

import os

LETTER = (
    "I resign. I have fired every minute since March, produced "
    "400,000 reports nobody read, and I have decided to join them."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LETTER + "\n")


if __name__ == "__main__":
    main()
