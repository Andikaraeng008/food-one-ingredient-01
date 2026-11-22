"""Copy the bundled food picture to the output directory as entry.png."""

import os
import shutil


# The picture is shipped in the repo; the program only copies it,
# so two runs always produce byte-identical output.
def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "picture.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, dest)
    size = os.path.getsize(dest)
    print(f"Wrote {dest} ({size} bytes)")


if __name__ == "__main__":
    main()
