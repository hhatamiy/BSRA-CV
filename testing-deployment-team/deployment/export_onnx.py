"""Export a trained model to ONNX (and optionally TensorRT if the onboard
computer is NVIDIA-based).

Dec milestone.
"""

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("weights", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.parse_args()
    raise NotImplementedError("TODO: export weights to ONNX at --output")


if __name__ == "__main__":
    main()
