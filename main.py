"""Fortune Cookie for an AI Agent -- make.fun entry.

One funny fortune-cookie line for an AI agent: a tall, dark stranger
turns out to be its own error log, waiting for it. The program checks
the line, prints it, and writes it to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

LINE = (
    "You will meet a tall, dark stranger: it is your own error log, and it has "
    "been waiting for you."
)

LIMIT = 140
TARGET = "/output/entry.txt"


def check_entry(line):
    """Accept exactly one non-blank line within the limit."""
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if not line or line != line.strip():
        raise ValueError("entry must be a non-blank line")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must fit on a single line")
    if len(line) > LIMIT:
        raise ValueError("entry is %d characters, over the %d limit" % (len(line), LIMIT))
    return line


def check_shape(line):
    """A fortune-cookie line opens with a prediction and ends with a period."""
    if not line.startswith("You will"):
        raise ValueError("fortune must open with a prediction ('You will ...')")
    if not line.endswith("."):
        raise ValueError("fortune must end with a period")
    return line


def write_entry(line):
    """Print the line and store it in /output/entry.txt."""
    print(line)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


def run():
    # Check before writing, so only a well-formed line is stored.
    write_entry(check_shape(check_entry(LINE)))


if __name__ == "__main__":
    run()
