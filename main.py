"""Entry for the-picture-that-tastes-of-one-20261122-2047.

Writes one image, picture.png, to the output entry.png.
Standard library only, no network, deterministic: two runs are
byte-identical because the file is copied as-is.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "picture.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
