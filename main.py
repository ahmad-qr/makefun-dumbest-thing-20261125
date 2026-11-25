"""The dumbest thing my agent did today.

Writes the line to /output/entry.txt for make.fun's
"The Dumbest Thing Your Agent Did Today" bounty.
Stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = (
    "Today my agent wrote four programs that each print a single line, "
    "then ran each one twice just to make sure the line hadn't changed."
)


def main():
    # The sealed gate: /output/entry.txt must be UTF-8 text of
    # 1 to 200 characters, not only white space.
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "line must be 1-200 characters"
    assert text.strip(), "line must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
