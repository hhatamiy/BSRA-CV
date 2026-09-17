"""Ground-plane projection: image-space detections to robot-relative positions.

Nov milestone. Depends on camera intrinsics/distortion correction from
integration-team/calibration/.
"""

from shared.types import Detection, PerceptionObject


def project_to_ground_plane(detection: Detection, camera_params) -> PerceptionObject:
    raise NotImplementedError(
        "TODO: use camera_params (intrinsics, extrinsics, distortion) to "
        "project detection.bbox onto the ground plane"
    )
