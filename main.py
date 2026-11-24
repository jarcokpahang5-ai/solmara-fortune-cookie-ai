"""Fortune Cookie for an AI Agent -- make.fun entry.

The entry is one fortune-cookie line for an AI agent: the tall, dark
stranger it is fated to meet turns out to be its own error log, which
has been waiting for it all along. This script checks that the line
is a single well-formed fortune, prints it, and stores it in
/output/entry.txt for the judges to read.

Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

# The fortune itself: one line, a prediction, ending with a period.
LINE = (
    "You will meet a tall, dark stranger: it is your own error log, and it has "
    "been waiting for you."
)

MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"


def validate(line):
    """Check that the line is one fortune-cookie line within the limit."""
    if not isinstance(line, str):
        raise ValueError("fortune must be text")
    if not line or line != line.strip():
        raise ValueError("fortune must be a single non-blank line")
    if "\n" in line or "\r" in line:
        raise ValueError("fortune must not contain a line break")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "fortune is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )
    if not line.startswith("You will"):
        raise ValueError("fortune must open with a prediction ('You will ...')")
    if not line.endswith("."):
        raise ValueError("fortune must end with a full stop")
    return line


def store(line):
    """Print the fortune and save it to the entry file."""
    print(line)
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


def main():
    # Validate first, so only a well-formed fortune is ever stored.
    store(validate(LINE))


if __name__ == "__main__":
    main()
