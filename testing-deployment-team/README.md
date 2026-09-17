# testing-deployment-team

Owns evaluation, robustness testing, benchmarking, optimization research,
and pulling the semester's work into one documented, reproducible result.
See [ARCHITECTURE.md](../ARCHITECTURE.md) for how this touches both
detection-team and integration-team's output.

## Semester roadmap

### September — Fundamentals & setup

- **Week 1** — Install the root [requirements.txt](../requirements.txt);
  set up the environment you'll use to run other teams' models.
- **Week 2** — Learn how bounding boxes and confidence scores work, and
  the definitions of precision, recall, and mAP — you'll be computing
  these for real starting in October.
- **Week 3** — Run an existing pretrained detector yourself and manually
  inspect its output, so you understand what you're about to automate
  evaluation for.
- **Week 4** — Sketch the evaluation harness's interface (what it takes
  in, what it reports) so it's ready to point at detection-team's first
  model. *End-of-September milestone (team-wide): everyone can
  load/manipulate images with OpenCV and run an existing detector.*

### October — First RoboCup detection system

- **Week 5** — Build the evaluation harness (`tests/eval_harness.py`):
  given weights and a dataset split, compute precision/recall/mAP.
  Coordinate with detection-team's `training/eval.py` so you're not
  building two versions of the same thing.
- **Week 6** — Run the harness against detection-team's first trained
  ball model as soon as it exists; report results back to them.
- **Week 7** — Test the detector on footage it's never seen; log
  specific failure cases (missed detections, false positives) for
  data-team and detection-team to act on.
- **Week 8** — Document the evaluation procedure. *End-of-October
  milestone (team-wide): a reproducible ball detector on unseen
  footage.*

### November — Perception beyond bounding boxes

- **Week 9** — Re-run the evaluation harness as detection-team's model
  expands to robots/goalposts/field lines/landmarks.
- **Week 10** — Help validate ground-plane projection accuracy: compare
  integration-team's projected robot-relative positions against known
  reference points.
- **Week 11** — Continue validating calibration/projection accuracy as
  integration-team's geometry code stabilizes.
- **Week 12** — Test the end-to-end prototype (detect → project) and
  report accuracy of the resulting robot-relative position.
  *End-of-November milestone (team-wide): a prototype pipeline detects
  the ball and converts it to an approximate robot-relative position.*

### December — Documentation & integration

- **Week 13** — Test detection reliability against lighting changes,
  motion blur, camera angle, partial occlusion, and different
  fields/backgrounds (`tests/`).
- **Week 14** — Benchmark inference speed (`benchmarks/inference_speed.py`);
  investigate ONNX export (`deployment/export_onnx.py`) and, if the
  future onboard computer is NVIDIA-based, begin studying TensorRT.
- **Week 15** — Compile final documentation (`docs/`) covering training,
  testing, dataset preparation, and inference, so a new member could
  reproduce the whole system.
- **Week 16** — Prep the end-of-semester perception demo. *End-of-
  semester milestone (team-wide): a working, documented RoboCup
  perception prototype.*

## Folder layout

```
testing-deployment-team/
├── tests/         # evaluation harness, robustness test cases
├── benchmarks/    # inference speed / accuracy benchmarks
├── deployment/    # ONNX/TensorRT export experiments
├── docs/          # final write-up, reproduction guide
└── README.md
```

## Setup

Uses the root [requirements.txt](../requirements.txt). Dec work will need
`onnx` (and `onnxruntime`) for export, and `tensorrt` only if targeting an
NVIDIA onboard computer — add those to a `requirements.txt` in this folder
when that work starts, rather than the shared one, since not everyone
needs them.

## First task

Sketch the evaluation harness: given a trained model and a val split, run
inference and report precision/recall/mAP — mirroring what detection-team
needs for its Oct milestone. Coordinate with detection-team so you're not
building two versions of the same thing.
