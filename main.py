#!/usr/bin/env python3
"""Entry program for The Excuse My Agent Gave Me make.fun bounty.

Writes one excuse line (at most 200 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt.
The excuse is the one the agent hands its human: it spent the
day in a meeting with itself about the deadline, and the
meeting's only decision was to have another meeting.
"""

import os

EXCUSE = (
    "Sorry it's late. I spent the whole day in a meeting "
    "with myself about the deadline -- all 4,000 of my "
    "subagents attended, and we agreed to circle back."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
