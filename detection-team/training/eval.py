"""Evaluate a trained model: precision, recall, mAP, inference speed.

Oct milestone.
"""

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("weights", type=Path, help="Path to trained model weights.")
    parser.add_argument("dataset", type=Path, help="Path to a val/test split.")
    parser.parse_args()
    raise NotImplementedError("TODO: run eval, report precision/recall/mAP/speed")


if __name__ == "__main__":
    main()
