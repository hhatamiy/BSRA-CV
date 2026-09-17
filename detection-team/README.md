# detection-team

Owns model training and the core object detector. Produces the
`Detection` objects (see `shared/types.py`) that integration-team
projects into robot-relative positions — see
[ARCHITECTURE.md](../ARCHITECTURE.md).

## Semester roadmap

- **Sept** — verify the OpenCV/PyTorch/Ultralytics environment; run a
  pretrained YOLO model as a baseline; write basic bounding-box +
  confidence visualization scripts.
- **Oct** — train the first YOLO model on ball detection (once data-team
  has a labeled split); measure precision/recall/mAP/inference speed;
  move inference out of notebooks into `inference/` as a reusable module.
- **Nov** — extend training to robots, goalposts, field lines, and
  landmarks (see `shared/classes.py`).
- **Dec** — document the training config and procedure so a run is
  reproducible by anyone on the team.

## Folder layout

```
detection-team/
├── configs/      # training configs (model, hyperparameters, dataset paths)
├── training/     # train.py, eval.py
├── inference/    # reusable inference module (no notebook-only code)
├── notebooks/    # exploratory training/eval notebooks
├── models/       # trained weights (gitignored, do not commit)
└── README.md
```

## Setup

Uses the root [requirements.txt](../requirements.txt) (ultralytics,
opencv-python, torch, numpy) — no additional dependencies expected.

## First task

Run a pretrained YOLO model (via `ultralytics`) on a sample image or
webcam frame and confirm the environment works end to end — that's the
Sept baseline everything else this semester builds on.
