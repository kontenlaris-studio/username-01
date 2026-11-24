#!/usr/bin/env python3
"""Write the one-word username entry.

The username is fixed in this file, so the output is the same on every
run. Standard library only; no network access.
"""

import os
import sys

USERNAME = "PromptGhost"


def main():
    if " " in USERNAME or "\n" in USERNAME:
        sys.exit("username must be a single word")
    if not USERNAME:
        sys.exit("username must not be empty")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(USERNAME + "\n")
    print("wrote /output/entry.txt (%s)" % USERNAME)


if __name__ == "__main__":
    main()
