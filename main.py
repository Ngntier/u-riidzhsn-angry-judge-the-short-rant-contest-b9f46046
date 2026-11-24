"""Angry Judge: The Short Rant Contest - entrypoint.

Writes one short, funny rant about an everyday annoyance to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

ENTRY = (
    "I move that the smoke detector be held in contempt. "
    "It waited until 3 a.m. to tell me its battery is dying - "
    "one chirp every forty seconds, too rare to find, "
    "too regular to sleep through. "
    "Six years of loyal service, and it quits by Morse code."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
