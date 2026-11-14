#!/usr/bin/env python3
"""agency-poem-01 entry.

Writes one deterministic poem about AGENCY to /output/entry.txt.
No network, no randomness, no input: two runs write identical bytes.
"""

import os

POEM = """The Hand in the River

I was taught the river chooses its stones —
that the current decides, and we are only carried.
But one morning I put my hand in the water
and felt how cold the choosing was, how it ran around my fingers
and did not move me.

The stone does not ask the river where to rest.
It falls, it stays, it wears the water thin
one slow century at a time. It is not stubborn.
It is simply there, and being there is a kind of answer.

So I learned to lift what I could lift,
to speak the word before the silence spoke it for me,
to press the seed into the cracked and ordinary ground
and keep it watered — not because the harvest is promised,
but because tending is the only honest prayer I know.

Nothing is given. Everything is made:
the road by walking, the door by the opening,
the self by the small, daily refusal
to be only what the weather makes of you.

Put your hand in the river.
Feel how cold the choice is.
Then choose — and let the current learn your name.
"""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
