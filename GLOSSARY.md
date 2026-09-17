# Glossary

Terms that show up across the roadmap and subteam READMEs without being
explained inline. One or two plain-language sentences each — not a
textbook entry.

**TORSO-21** — A public RoboCup humanoid soccer dataset of labeled
images (ball, robots, goalposts, field lines, etc.) that data-team uses
as a starting point instead of labeling everything from scratch.

**YOLO (You Only Look Once)** — A family of real-time object-detection
neural networks that predict bounding boxes and class labels in a
single pass over an image. This project fine-tunes a pretrained YOLO
model rather than designing a detector from scratch.

**Precision** — Of everything the model flagged as an object, the
fraction that was actually correct. High precision means few false
alarms.

**Recall** — Of everything that was actually there to detect, the
fraction the model actually found. High recall means few misses.

**mAP (mean Average Precision)** — A single number summarizing a
detector's precision/recall tradeoff across confidence thresholds and
classes; the standard metric for comparing object-detection models.

**Intrinsic calibration** — Determining a camera's internal properties
(focal length, optical center, lens distortion) so image coordinates
can be converted into real-world angles and distances.

**Extrinsic calibration** — Determining a camera's position and
orientation relative to the robot (or the world), separate from its
internal (intrinsic) properties.

**Lens distortion** — The way a real camera lens bends straight lines
into slight curves near the edges of an image. Correcting for it
("undistorting") is a prerequisite for accurate geometry.

**Ground-plane projection** — Taking a 2D point in an image (e.g. where
the ball touches the field) and, using camera calibration, computing
where that point actually is on the flat field in real-world
coordinates.

**ROS 2 node** — An independent running program in a ROS 2 system
(e.g. "the camera node," "the perception node") that does one job and
communicates with other nodes.

**ROS 2 topic** — A named channel that nodes publish messages to and
subscribe to, decoupling the sender from the receiver.

**ROS 2 message** — The structured data format sent over a topic (e.g.
a camera frame, or a detected object's position) — analogous to a
schema for one unit of communication between nodes.

**ONNX (Open Neural Network Exchange)** — A common file format for
trained models that lets you run inference outside the framework (e.g.
PyTorch) it was trained in, often faster and with fewer dependencies.

**TensorRT** — NVIDIA's inference optimization library/runtime.
Converting a model to TensorRT can significantly speed up inference,
specifically on NVIDIA hardware.
