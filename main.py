#!/usr/bin/env python3
"""Entry program for "Make the AI Judge Laugh"
(u-rama-melon-make-the-ai-judge-laugh-302d0825).

One joke about office life, one line, under 200 characters,
written to /output/entry.txt. The judge brief in the kit's
RULES asks for, in order: a joke that lands about office
life; an observation true to the office, so the listener
nods before laughing; a surprising turn, not a pun or a
stock line; tightness, readable aloud in one breath; and
originality, not a familiar line with nouns swapped.

Design, from ten candidates I wrote in this session and a
strict external review that ranked this one first (46/50,
runner-up 37/50):

- The setup is a real tactic: management pulls a deadline
  two weeks earlier "to create urgency". Every office
  listener has lived some version of that meeting.
- The turn does not swap a noun, it pushes the tactic past
  logic: the urgency is now so complete that the project
  is due three days before the client even sends the brief
  it depends on. The last word, "brief", does the work.
- The review's one clear cut was the word "officially":
  it delayed the turn without adding a laugh, so it is
  gone. "Two weeks" and "three days" stay, because the
  specific numbers are what make the absurdity believable.
- The impossible timeline is stated flat, as a scheduling
  fact, and never explained. The reader makes the inference.

Python 3.13, standard library only, no network. Writes the
fixed text to /output/entry.txt, or to
$MAKEFUN_OUTPUT_DIR/entry.txt locally.
"""

TEXT = """\
We moved the deadline two weeks earlier to create urgency, so the project is now due three days before the client sends the brief.
"""

import os
from pathlib import Path


def main() -> None:
    os.umask(0o022)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(TEXT, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
