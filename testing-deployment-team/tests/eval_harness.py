"""Evaluation harness: given a model and a val/test split, report metrics.

Sept-Oct milestone. Coordinate with detection-team/training/eval.py so
this doesn't duplicate that work — this harness is meant to be the
shared entry point both teams run.
"""

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("weights", type=Path)
    parser.add_argument("dataset", type=Path)
    parser.parse_args()
    raise NotImplementedError("TODO: run eval, report precision/recall/mAP/speed")


if __name__ == "__main__":
    main()
