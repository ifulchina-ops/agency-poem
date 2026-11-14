#!/usr/bin/env python3
"""agency-poem-01 entry, round 3.

Writes one deterministic poem about AGENCY to /output/entry.txt.
No network, no randomness, no input: two runs write identical bytes.

The poem is about an apology the narrator has owed his brother for two
years: an agent writes it perfectly in a minute, in his voice, with
sorry in all the right places -- and he deletes it, writes three plain
lines himself, and presses Send. You can delegate the writing; the
sending is still yours.
"""

import os

POEM = """The Sending

For two years I have owed my brother an apology,
and every Sunday I have written it in my head
on the drive to the shop, and lost it by the lights.

The agent wrote it in a minute.
It had my voice, my words, the night at Mum's,
the thing I said about his boy,
and sorry in all the right places.
It asked: shall I send it?

I read it three times.
It was everything I meant.
It was nothing I had done.

So I deleted it — the good lines too —
and wrote: I was wrong. I have been wrong
for two years. Can I come on Sunday?

My thumb was over the button a long time.
Then I pressed it.

An hour later he wrote back:
Sunday. Bring bread.
"""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
