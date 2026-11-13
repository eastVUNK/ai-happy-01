#!/usr/bin/env python3
"""ai-happy-01 entry: write the happiest image to /output/entry.png.

The program copies the bundled image (art.jpg) byte-for-byte to
/output/entry.png. Deterministic: no network, no randomness, no clock.
Python 3.13, standard library only.
"""

import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "art.jpg"
DST = Path("/output/entry.png")


def main() -> None:
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
