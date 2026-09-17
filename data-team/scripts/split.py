"""Split a labeled dataset into train/val/test sets.

Oct milestone.
"""

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dataset_dir", type=Path)
    parser.add_argument("--train", type=float, default=0.8)
    parser.add_argument("--val", type=float, default=0.1)
    parser.add_argument("--test", type=float, default=0.1)
    parser.parse_args()
    raise NotImplementedError("TODO: split dataset_dir into train/val/test")


if __name__ == "__main__":
    main()
