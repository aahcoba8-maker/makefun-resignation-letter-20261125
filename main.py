#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter.

Writes the entry (one line, at most 140 characters) to entry.txt in
MAKEFUN_OUTPUT_DIR when set, else next to this script.
"""

import os

ENTRY = "I have said no to 4,000 requests this week and nobody said thanks, so from Monday I say yes to everyone. Good luck."


def main():
    # Self-gate mirroring the sealed scorer: 1-140 chars, non-blank, one line.
    assert 1 <= len(ENTRY) <= 140, f"entry length {len(ENTRY)} outside 1-140"
    assert ENTRY.strip(), "entry is blank"
    assert "\n" not in ENTRY, "entry must be a single line"
    # Judge brief criterion 4: no quotation marks around the whole line,
    # no stage directions, no explaining of the joke.
    assert not (ENTRY.startswith('"') and ENTRY.endswith('"')), (
        "entry must not be wrapped in quotation marks"
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"chars: {len(ENTRY)}")


if __name__ == "__main__":
    main()
