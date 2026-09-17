# testing-deployment-team

Owns evaluation, robustness testing, benchmarking, optimization research,
and pulling the semester's work into one documented, reproducible result.
See [ARCHITECTURE.md](../ARCHITECTURE.md) for how this touches both
detection-team and integration-team's output.

## Semester roadmap

- **Sept–Oct** — build an evaluation harness alongside detection-team's
  early training runs, so results are comparable run to run.
- **Nov** — help validate calibration/projection accuracy
  (integration-team's ground-truth checks).
- **Dec** — test detection reliability against lighting changes, motion
  blur, camera angle, occlusion, and background variation; benchmark
  inference speed; investigate ONNX export and, if the onboard computer
  is NVIDIA-based, TensorRT; compile final documentation so a new member
  could reproduce the whole system; prep the end-of-semester perception
  demo.

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
