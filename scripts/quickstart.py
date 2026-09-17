"""Run one sample image through as much of the real BSRA-CV pipeline as
currently exists.

WHAT THIS RUNS TODAY:
  - Loads an image (yours, or ultralytics' bundled sample image).
  - Runs a stock pretrained YOLO model via the `ultralytics` package.
  - Converts the raw output into this repo's shared `Detection` type
    (shared/types.py) and prints it.

This intentionally bypasses detection-team/inference/detector.py and
calls ultralytics directly, because that module is still a stub (see
ARCHITECTURE.md's "Pipeline status" table) — as of writing, nothing in
this repo can load or run a model end to end on its own yet. Once
detector.py is implemented, this script should call it instead.

WHAT THIS DOES NOT COVER (because the code doesn't exist yet):
  - A RoboCup-trained model: this uses YOLO's stock pretrained COCO
    weights, which do NOT know about soccer balls, goalposts, or field
    lines the way a fine-tuned model eventually will. Detections you see
    are whatever COCO classes (person, sports ball, etc.) happen to
    appear in the image.
  - Camera calibration / lens distortion correction
    (integration-team/calibration/).
  - Ground-plane projection to a robot-relative position
    (integration-team/geometry/).
  - The ROS 2 perception message / nodes
    (integration-team/messages/, integration-team/ros2_nodes/).

As each of those gets built out for real, extend this script to call
into it instead of skipping it, so it stays the one command that proves
the current end-to-end state of the pipeline.
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from shared.types import BoundingBox, Detection


def run(image_path: Path) -> list[Detection]:
    from ultralytics import YOLO

    model = YOLO("yolov8n.pt")  # pretrained COCO weights, auto-downloaded on first run
    results = model.predict(source=str(image_path), verbose=False)

    detections = []
    for result in results:
        for box in result.boxes:
            x_min, y_min, x_max, y_max = box.xyxy[0].tolist()
            detections.append(
                Detection(
                    class_name=result.names[int(box.cls[0])],
                    confidence=float(box.conf[0]),
                    bbox=BoundingBox(x_min=x_min, y_min=y_min, x_max=x_max, y_max=y_max),
                )
            )
    return detections


def default_sample_image() -> Path:
    try:
        from ultralytics.utils import ASSETS

        return ASSETS / "bus.jpg"
    except (ImportError, AttributeError) as e:
        raise SystemExit(
            "No --image given and couldn't locate ultralytics' bundled sample "
            f"image ({e}). Pass one explicitly: "
            "python scripts/quickstart.py path/to/image.jpg"
        ) from e


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "image",
        type=Path,
        nargs="?",
        default=None,
        help="Path to a sample image. If omitted, uses ultralytics' bundled sample image.",
    )
    args = parser.parse_args()

    image_path = args.image or default_sample_image()
    if not image_path.exists():
        parser.error(f"Image not found: {image_path}")

    print(f"Running pretrained (stock COCO, not RoboCup-trained) YOLO on: {image_path}\n")
    detections = run(image_path)

    if not detections:
        print("No detections.")
    for d in detections:
        print(d)


if __name__ == "__main__":
    main()
