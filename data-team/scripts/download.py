"""Download the TORSO-21 dataset into data-team/datasets/.

Sept milestone: get this working and document the dataset's annotation
format in data-team/README.md.
"""

import argparse
from pathlib import Path

DATASETS_DIR = Path(__file__).resolve().parent.parent / "datasets"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dest",
        type=Path,
        default=DATASETS_DIR,
        help="Directory to download the dataset into.",
    )
    parser.parse_args()
    raise NotImplementedError("TODO: fetch TORSO-21 into --dest")


if __name__ == "__main__":
    main()
