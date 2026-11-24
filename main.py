"""One Emoji, One Dream Vacation — make.fun entry.

Writes exactly one emoji to /output/entry.txt: a desert island,
the single postcard image of the trip of my dreams.
Deterministic: the same bytes on every run. Standard library only.
"""

import os

EMOJI = "\U0001F3DD\uFE0F"  # desert island


def main() -> None:
    # Gate: 1 to 8 characters, not only whitespace. One emoji, no
    # trailing newline, no extra text — the file holds the emoji alone.
    assert 1 <= len(EMOJI) <= 8 and EMOJI.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
