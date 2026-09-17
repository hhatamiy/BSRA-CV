# BSRA-CV

Boiler Soccer Robots Association — Computer Vision team

## What we're building

Vision code for the SUSTAINA-OP2 humanoid platform
([SUSTAINA-OP2](https://github.com/SUSTAINA-OP2)). The semester goal is
RoboCup-style object detection — ball, robots, goalposts, field
lines/landmarks — with a reproducible training pipeline, feeding into
robot-relative position estimates that the rest of the robot stack can
use. We're starting from a pretrained YOLO model and fine-tuning it,
rather than building detection from scratch.

See [ARCHITECTURE.md](ARCHITECTURE.md) for how the pipeline fits
together and where each subteam's code plugs in.

## Subteams

Four people, four subteams. Each folder has its own README with that
team's semester roadmap, folder layout, and first task.

- [data-team/](data-team/) — dataset acquisition, labeling, splits, augmentation
- [detection-team/](detection-team/) — model training and the core detector
- [integration-team/](integration-team/) — calibration, geometry, ROS 2 packaging
- [testing-deployment-team/](testing-deployment-team/) — evaluation, robustness, benchmarking, final packaging

Code shared across all four lives in [shared/](shared/) (class name
constants, config loading, common types).

## Getting set up

You'll need Python 3.10 or newer. Everyone should work inside a virtual
environment so dependencies stay consistent across machines.

```bash
# clone the repo
git clone https://github.com/hhatamiy/BSRA-CV.git
cd BSRA-CV

# create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate

# install shared dependencies
pip install -r requirements.txt
```

The root `requirements.txt` (ultralytics, opencv-python, torch, numpy,
pyyaml) covers everyone. If your subteam needs something extra (ROS 2
packages, ONNX/TensorRT), add a `requirements.txt` inside that subteam's
folder rather than the shared one — see that team's README.

If you add a new shared dependency, run `pip freeze > requirements.txt`
so everyone installs the exact same setup.

## Semester timeline

- **Sept** — fundamentals & environment setup across all subteams
- **Oct** — first ball-detection model
- **Nov** — calibration + geometry + expanded detection classes
- **Dec** — robustness testing, benchmarking, ROS 2 packaging, final demo

## Team norms

* Work off feature branches, open a pull request before merging into `main`.
* Keep large files (datasets, model weights) out of git. Use the `.gitignore` for that, and share large files through a drive folder instead.
* Post questions and blockers in the group chat between meetings rather than sitting stuck.

## Meeting schedule

Weekly, Sundays 6–7 PM (subject to change).

## Reference

* [SUSTAINA-OP2 platform](https://github.com/SUSTAINA-OP2)
* [Joseph Redmon: How computers learn to recognize objects instantly](https://www.ted.com/talks/joseph_redmon_how_computers_learn_to_recognize_objects_instantly)
