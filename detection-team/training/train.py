"""Train a YOLO model on a labeled dataset split.

Oct milestone: first ball-detection model. Config (model, hyperparameters,
dataset paths) should live in detection-team/configs/ and load via
shared.config.load_config, not be hardcoded here.
"""

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("config", type=Path, help="Path to a training config YAML.")
    parser.parse_args()
    raise NotImplementedError("TODO: load config, train with ultralytics YOLO")


if __name__ == "__main__":
    main()
