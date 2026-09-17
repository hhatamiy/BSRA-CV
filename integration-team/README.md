# integration-team

Owns calibration, geometry, and ROS 2 packaging: turning detection-team's
image-space `Detection`s into robot-relative `PerceptionObject`s (see
`shared/types.py`) and publishing them for the rest of the robot stack.
See [ARCHITECTURE.md](../ARCHITECTURE.md) for the full pipeline.

## Semester roadmap

- **Sept** — ROS 2 environment setup; review image/message concepts
  (topics, message types, nodes).
- **Nov** — camera intrinsic calibration and lens distortion correction;
  define coordinate systems and ground-plane projection; define the
  perception message schema; write the first ROS 2 nodes for camera
  input and detections.
- **Dec** — package the trained detector as a clean ROS 2 node/module
  alongside the projection code.

## Folder layout

```
integration-team/
├── calibration/   # camera intrinsics, distortion correction
├── geometry/      # coordinate transforms, ground-plane projection
├── ros2_nodes/    # ROS 2 nodes (camera input, detection, projection)
├── messages/      # perception message definitions
└── README.md
```

## Setup

Uses the root [requirements.txt](../requirements.txt) plus ROS 2 itself
(install per your OS/distro — not pip-installable). Add any
integration-specific Python packages (e.g. `rclpy` extras) to a
`requirements.txt` in this folder once the Nov ROS 2 work starts.

## First task

Get a ROS 2 workspace building and a minimal publisher/subscriber pair
running locally — that's the Sept environment-setup milestone this
subteam's Nov work depends on.
