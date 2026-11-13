"""make.fun entry: "Make the AI judge laugh" (ai-joke-03).

Writes one joke -- a one-liner about AI coding agents, the tools
developers work beside every day -- to /output/entry.txt. The file
holds exactly the joke text (125 characters, no trailing newline).
No network, no randomness, so both runs write identical bytes.
"""

import os

JOKE = (
    "My AI coding agent fixed my bug in three seconds, then spent forty "
    "minutes explaining why the bug was my fault. It was right."
)

DST = "/output/entry.txt"

os.makedirs("/output", exist_ok=True)
# Exact bytes, no trailing newline, so the output is deterministic.
with open(DST, "w", encoding="utf-8") as f:
    f.write(JOKE)
print("wrote", DST)
