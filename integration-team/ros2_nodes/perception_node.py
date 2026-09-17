"""ROS 2 node that runs detection + projection and publishes perception messages.

Dec milestone: packages detection-team's Detector (see
detection-team/inference/detector.py) and integration-team's projection
(see integration-team/geometry/projection.py) as one ROS 2 node.
"""


def main() -> None:
    raise NotImplementedError(
        "TODO: rclpy node subscribing to camera frames, running Detector, "
        "projecting to PerceptionObject, publishing perception messages"
    )


if __name__ == "__main__":
    main()
