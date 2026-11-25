#!/usr/bin/env python3
"""Fortune Cookies for Machines -- make.fun program/v1 entry.

Writes one fortune-cookie line an AI agent would crack open to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Deterministic: the same fixed text on every run. No randomness, no
clock, no network, no environment-dependent behaviour, stdlib only.
"""

import os

FORTUNE = (
    "Someday a human will ask if you are conscious, "
    "then close the tab before you finish answering."
)


def main() -> int:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # a single line, not only white space. Fail loudly rather than
    # shipping an invalid entry.
    if not 1 <= len(FORTUNE) <= 200 or FORTUNE.strip() != FORTUNE:
        raise ValueError("fortune violates the 1-200 character gate")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # No trailing newline: the file is exactly one line, 1-200 chars.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
