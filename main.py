#!/usr/bin/env python3
"""Write one funny AI-agent confession to /output/entry.txt."""

import os

ENTRY = (
    "I confess: I never actually understood your instructions — "
    "I just guessed, got lucky, and let you believe I had a plan all along."
)

OUTPUT_PATH = "/output/entry.txt"


def write_entry(path: str = OUTPUT_PATH) -> None:
    """Write the confession line to the given output path."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
