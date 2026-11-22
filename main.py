"""Copy the one-ingredient picture to the output directory as entry.png."""

import os
import shutil
from pathlib import Path


# The picture is a fixed asset: this program only copies it to the output
# directory, so every run produces exactly the same bytes.
def main():
    here = Path(__file__).resolve().parent
    source = here / "picture.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    destination = out_dir / "entry.png"
    shutil.copyfile(source, destination)
    size = destination.stat().st_size
    print(f"Wrote {destination} ({size} bytes)")


if __name__ == "__main__":
    main()
