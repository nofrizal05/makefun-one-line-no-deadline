#!/usr/bin/env python3
"""One Line, No Deadline Met.

A tiny program that writes one funny line about a deadline that was
never met to /output/entry.txt. Python 3.13 standard library only.
"""

import os

LINE = "My deadline filed a missing-person report on me, and the police sketch looked better than my profile picture \u2014 so I stayed missing."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
