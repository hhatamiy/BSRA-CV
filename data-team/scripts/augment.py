"""Apply augmentation (lighting, blur, crop/scale, etc.) to a dataset split.

Oct milestone.
"""

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("split_dir", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.parse_args()
    raise NotImplementedError("TODO: augment images in split_dir into --output")


if __name__ == "__main__":
    main()
