"""Camera intrinsic calibration and lens distortion correction.

Nov milestone. Produces the camera_params consumed by
integration-team/geometry/projection.py.
"""

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "images_dir", type=Path, help="Directory of checkerboard calibration images."
    )
    parser.add_argument("--output", type=Path, required=True, help="Where to save camera params.")
    parser.parse_args()
    raise NotImplementedError("TODO: run OpenCV checkerboard calibration, save intrinsics")


if __name__ == "__main__":
    main()
