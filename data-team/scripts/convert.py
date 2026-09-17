"""Convert raw annotation formats (e.g. TORSO-21) into YOLO label format.

Sept-Oct milestone, once the dataset schema is documented in
data-team/README.md.
"""

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_dir", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.parse_args()
    raise NotImplementedError("TODO: convert annotations in source_dir into --output")


if __name__ == "__main__":
    main()
