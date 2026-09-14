# BSRA-CV

Boiler Soccer Robots Association — Computer Vision team

## What we're building

Vision code for the SUSTAINA-OP2 humanoid platform. The goal is real-time object detection so the robot can identify the ball, field lines, and other robots during play. We're starting from a pretrained YOLO model and fine-tuning it on the specific objects our robot needs to see, rather than building detection from scratch.

## Getting set up

You'll need Python 3.10 or newer. Everyone should work inside a virtual environment so our dependencies stay consistent across machines.

```bash
# clone the repo
git clone https://github.com/hhatamiy/BSRA-CV.git
cd BSRA-CV

# create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate

# install dependencies
pip install -r requirements.txt
```

Core packages: `ultralytics`, `opencv-python`, `torch`, `numpy`. If you add a new dependency, run `pip freeze > requirements.txt` afterward so everyone else can install the exact same setup.

## Project structure

```
BSRA-CV/
├── data/           # training images, labeled datasets (gitignored, don't commit raw data)
├── models/         # saved model weights and checkpoints (gitignored)
├── notebooks/      # exploratory work, experiments
├── src/            # actual detection pipeline code
├── docs/           # notes, meeting summaries, references
├── requirements.txt
└── README.md
```

## Team norms

* Work off feature branches, open a pull request before merging into `main`.
* Keep large files (datasets, model weights) out of git. Use the `.gitignore` for that, and share large files through a drive folder instead.
* Post questions and blockers in the group chat between meetings rather than sitting stuck.

## Meeting schedule

Weekly, Sundays 6–7 PM (subject to change).

## Reference

* [SUSTAINA-OP2 platform](https://github.com/SUSTAINA-OP2)
* [Joseph Redmon: How computers learn to recognize objects instantly](https://www.ted.com/talks/joseph_redmon_how_computers_learn_to_recognize_objects_instantly)
