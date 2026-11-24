#!/usr/bin/env python3
"""Fortune in a Pot — one kind, funny fortune for a houseplant.

Writes a single line (<=120 characters) to /output/entry.txt.
Deterministic, standard library only, no network, no environment reads.
"""

import os

# The fortune itself: a prediction about this plant's own future, told
# for the plant on the windowsill. "Your sunbeam" anchors it to this
# window, not any plant in any room. The joke is situational, not a pun:
# the keeper will take the credit for the sun's work, and the plant
# knows the truth. Warm, no doom, fortune cadence throughout.
FORTUNE = (
    "Your sunbeam has pencilled you in for a growth spurt, "
    "and your keeper takes the credit. Let them \u2014 you know the truth."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 120


def main() -> None:
    text = FORTUNE.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(
            "fortune must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("fortune must be a single line")
    if not text.strip():
        raise SystemExit("fortune must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the gate counts every character in the file.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print("wrote %d characters to %s" % (len(text), OUTPUT_PATH))


if __name__ == "__main__":
    main()
