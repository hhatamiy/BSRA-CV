# BSRA-CV

Boiler Soccer Robots Association — Computer Vision team

**New to the team? Start with [ONBOARDING.md](ONBOARDING.md)** — it
tells you what to read, in what order, and how to get set up.

## Leadership

- **Computer Vision Lead:** Hossein Hatami Yazd ([hhatamiy@purdue.edu](mailto:hhatamiy@purdue.edu))
- **Programming Director:** Adhitya Vasudevan ([adhiv2007@gmail.com](mailto:adhiv2007@gmail.com), [vasude29@purdue.edu](mailto:vasude29@purdue.edu))

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

Six people across four subteams. Each folder has its own README with
that team's semester roadmap, folder layout, and first task. See
[.github/CODEOWNERS](.github/CODEOWNERS) for who's on each one.

- [data-team/](data-team/) — dataset acquisition, labeling, splits, augmentation (Gabriela, Josephine)
- [detection-team/](detection-team/) — model training and the core detector (Suhaas, Aditya Mitra)
- [integration-team/](integration-team/) — calibration, geometry, ROS 2 packaging (Phil)
- [testing-deployment-team/](testing-deployment-team/) — evaluation, robustness, benchmarking, final packaging (Hossein)

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

# run the quickstart to confirm your environment works
python scripts/quickstart.py
```

`scripts/quickstart.py` runs a sample image through as much of the real
pipeline as currently exists — see its docstring for exactly what that
covers today (honestly, not much yet — see the "Pipeline status" table
in [ARCHITECTURE.md](ARCHITECTURE.md#pipeline-status)) and what it
doesn't. The first run downloads ~6MB of pretrained YOLO weights.

The root `requirements.txt` (ultralytics, opencv-python, torch, numpy,
pyyaml) covers everyone. If your subteam needs something extra (ROS 2
packages, ONNX/TensorRT), add a `requirements.txt` inside that subteam's
folder rather than the shared one — see that team's README.

If you add a new shared dependency, run `pip freeze > requirements.txt`
so everyone installs the exact same setup.

If you're writing tests or running lint locally, also install the dev
tools: `pip install -r requirements-dev.txt`. This isn't required just
to run inference or training.

## Semester timeline

By the end of Fall 2026 the CV team should be able to take RoboCup-style
camera footage, reliably detect important soccer-field objects, begin
converting those detections into robot-relative information, and have a
reproducible training/inference pipeline ready to integrate into the
full robot software stack.

- **Sept — Fundamentals & setup.** Every member can run the dev
  environment: OpenCV/PyTorch/Ultralytics installed, TORSO-21 explored,
  a pretrained detector running.
- **Oct — First RoboCup detection system.** A reproducible model that
  detects the soccer ball in unseen RoboCup-style footage.
- **Nov — Perception beyond bounding boxes.** Detection expands to
  robots/goalposts/field lines/landmarks; a prototype pipeline converts
  a ball detection into an approximate robot-relative position.
- **Dec — Documentation & integration.** Robustness testing, inference
  benchmarking, ONNX/TensorRT exploration, ROS 2 packaging, and enough
  documentation that a new member could reproduce the whole system.

Each subteam README has the full week-by-week breakdown for its slice
of this timeline: [data-team](data-team/README.md#semester-roadmap),
[detection-team](detection-team/README.md#semester-roadmap),
[integration-team](integration-team/README.md#semester-roadmap),
[testing-deployment-team](testing-deployment-team/README.md#semester-roadmap).

### Success criteria

By the end of the semester, the team should ideally have:

- A reproducible CV development environment
- A shared RoboCup dataset workflow
- A trained RoboCup object-detection model
- Reliable ball detection
- Initial goalpost/robot/field perception
- Basic camera calibration
- Basic ground-plane projection
- Quantitative model evaluation
- Initial ROS 2 integration
- Clear documentation allowing a new member to reproduce the system
- A final perception demonstration

## Team norms

* Work off feature branches, open a pull request before merging into `main`.
* Keep large files (datasets, model weights) out of git. Use the `.gitignore` for that, and share large files through a drive folder instead.
* Post questions and blockers in the group chat between meetings rather than sitting stuck.

## Meeting schedule

Weekly, Sundays 6–7 PM (subject to change).

**Open question:** now that the team is six people, worth deciding
whether to keep a single one-hour Sunday sync for everyone, or split
into a shorter full-team check-in plus separate subteam meetings.
Not decided yet — raise it at the next sync.

## Reference

* [SUSTAINA-OP2 platform](https://github.com/SUSTAINA-OP2)
* [Joseph Redmon: How computers learn to recognize objects instantly](https://www.ted.com/talks/joseph_redmon_how_computers_learn_to_recognize_objects_instantly)
