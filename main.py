"""Write one fixed one-line joke to the entry output file.

The joke text is a constant; this program only resolves the output
path (via OUTPUT_PATH, defaulting to /output/entry.txt), creates any
missing parent directories, and writes the joke exactly as-is, with
no trailing newline.
"""

import os
import sys
from pathlib import Path

JOKE = "The demo only ever worked while the agent was driving — the moment I took the keyboard, the audience realised I was just the loading screen."

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> int:
    path = Path(OUTPUT_PATH)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(JOKE, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
