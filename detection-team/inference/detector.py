"""Reusable inference module: image in, `Detection`s out.

This is what integration-team's ROS 2 node calls, and what
testing-deployment-team benchmarks — keep it notebook-free so both can
import it directly.
"""

from pathlib import Path

from shared.types import Detection


class Detector:
    def __init__(self, weights_path: str | Path) -> None:
        self.weights_path = Path(weights_path)
        raise NotImplementedError("TODO: load YOLO model from weights_path")

    def predict(self, image) -> list[Detection]:
        raise NotImplementedError("TODO: run inference, return list[Detection]")
