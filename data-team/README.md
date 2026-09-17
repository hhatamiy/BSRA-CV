# data-team

Owns dataset acquisition, labeling, splits, and augmentation for the
perception pipeline. See [ARCHITECTURE.md](../ARCHITECTURE.md) for how
this feeds into detection-team.

## Semester roadmap

- **Sept** — download and explore the [TORSO-21](https://github.com/bit-bots/TORSO-21-dataset)
  dataset; document its label format in this README.
- **Oct** — build train/val/test split scripts; implement augmentation
  (lighting, blur, crop/scale, etc.).
- **Nov–Dec** — extend the dataset with goalpost, robot, field-line, and
  landmark classes (see `shared/classes.py` for the canonical names);
  curate harder validation sets (varied lighting, occlusion, varied
  backgrounds) for testing-deployment-team to use in robustness testing.

## Folder layout

```
data-team/
├── datasets/     # raw and processed datasets (gitignored, do not commit)
├── scripts/      # download.py, convert.py, split.py, augment.py
├── labeling/     # labeling tool config/output
└── README.md
```

## Dataset schema

_To be filled in once the TORSO-21 dataset is downloaded and explored —
document the label format (annotation file structure, class list,
coordinate conventions) here so detection-team and testing-deployment-team
can rely on it._

## Setup

Uses the root [requirements.txt](../requirements.txt). No additional
dependencies yet — if a labeling tool or augmentation library needs one,
add it here and note it in this README.

## First task

Download the TORSO-21 dataset (see `scripts/download.py`) and document
its annotation format and class list in the "Dataset schema" section
above — that's the Sept milestone and what detection-team is waiting on.
