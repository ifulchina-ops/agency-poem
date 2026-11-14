#!/usr/bin/env python3
"""agency-poem-01 entry, round 2.

Writes one deterministic poem about AGENCY to /output/entry.txt.
No network, no randomness, no input: two runs write identical bytes.

The poem is about agency passing between people -- and between a person
and the agent that acts for her: a daughter who used to make every call
for her mother, and what it costs the helper when the mother takes her
own voice back.
"""

import os

POEM = """The Hands She Borrowed

For years she called me to call for her —
the clinic, the bank, the man about the roof.
My voice, her words. I was fluent in being her.

Then the small speaker on her table learned her name.
Now she asks it herself, each morning, slowly,
and it answers in a voice that is not mine.

I should be glad. I am glad.
But some evenings the phone doesn't ring,
and I miss being the hands she borrowed,
the proof that she still needed me.

She speaks now. My evenings are quieter.
She is louder.
"""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
