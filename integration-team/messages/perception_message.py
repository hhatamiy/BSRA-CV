"""Perception message schema published over ROS 2.

Nov milestone: define this schema, then generate/wire it as an actual
ROS 2 .msg (or use this as the Python-side shape if publishing via a
custom message package). Should stay a straightforward mapping from
shared.types.PerceptionObject.
"""

from shared.types import PerceptionObject


def to_ros_message(obj: PerceptionObject):
    raise NotImplementedError("TODO: convert PerceptionObject to the ROS 2 message type")
