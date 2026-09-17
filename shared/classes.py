"""Canonical object classes for the perception pipeline.

Detection, data labeling, and integration code should all import from
here rather than hardcoding class names or indices, so a class added by
one subteam is immediately visible to the others.
"""

BALL = "ball"
ROBOT = "robot"
GOALPOST = "goalpost"
FIELD_LINE = "field_line"
LANDMARK = "landmark"

CLASSES = [BALL, ROBOT, GOALPOST, FIELD_LINE, LANDMARK]

CLASS_TO_ID = {name: idx for idx, name in enumerate(CLASSES)}
ID_TO_CLASS = {idx: name for idx, name in enumerate(CLASSES)}
