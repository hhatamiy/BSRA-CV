"""Benchmark inference speed of a trained model.

Dec milestone.
"""

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("weights", type=Path)
    parser.add_argument("--runs", type=int, default=100)
    parser.parse_args()
    raise NotImplementedError("TODO: time inference over --runs, report avg/median/p95")


if __name__ == "__main__":
    main()
