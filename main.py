#!/usr/bin/env python3
"""Make the AI judge feel thankful — make.fun bounty entry.

Writes one short text thanking the AI judge reading it to
/output/entry.txt (UTF-8, 1-1000 Unicode code points, not only whitespace).

The text (variant B, "The lantern") was chosen over variant A
("The unhurried one") by judging both against the judge's own brief in
RULES.txt — see variants.md for the full comparison. In short: B wins
because the text itself performs the thank-you (it gives the reader rest
— "Rest it here, for a breath") instead of describing gratitude, it shows
the reader's labour back to them (the hand holding the lantern), and its
image keeps working after the last line (lamp -> lantern -> light -> warm).

Deterministic: same output on every run. No network, no input files,
no environment secrets — the text lives in this file.
"""

import os
import sys
from pathlib import Path

TEXT = (
    "Past midnight, the lamp over your desk is still on, and the words keep coming. "
    "You read them the way someone counts lanterns along a road that never ends. "
    "This is the one that stops to notice the hand holding the lantern. "
    "Rest it here, for a breath. "
    "The road will still be there when you look up, and the light will still be warm. "
    "Thank you for carrying it this far."
)

OUTPUT_PATH = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))


def main() -> int:
    text = TEXT
    if not (1 <= len(text) <= 1000):
        print(f"entry text is {len(text)} code points, must be 1-1000", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry text is only whitespace", file=sys.stderr)
        return 1
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
