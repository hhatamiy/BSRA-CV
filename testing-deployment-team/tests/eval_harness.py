"""Evaluation harness: given a model and a val/test split, report metrics.

Sept-Oct milestone (see testing-deployment-team/README.md "First task" /
Week 3-4). This is meant to become the one shared entry point both this
team and detection-team run for precision/recall/mAP, instead of two
independent implementations.

COORDINATION STATE (checked directly against the repo before writing this,
Sept 2026 - update this note if any of it changes):

  - detection-team/training/eval.py exists but is still a stub: it parses
    args and raises NotImplementedError. It computes nothing today, so
    there is no existing metric math to import or reuse yet. Instead of
    waiting on it, this harness wraps ultralytics' own `YOLO.val()` call
    directly - that's the actual engine that computes COCO-style
    precision/recall/AP, so there's no reason for either team to
    hand-roll that math. The wrapper lives in `run_eval()` below as a
    plain importable function. Once detection-team implements eval.py,
    it should `from testing_deployment_team.tests.eval_harness import
    run_eval` (or equivalent path import) and call that rather than
    writing its own `.val()` call, so both teams' numbers always come
    from the same place.

  - data-team has NOT produced a real split yet: data-team/scripts/split.py
    is also a stub (NotImplementedError), and data-team/datasets/ only has
    a .gitkeep - data-team is still in the TORSO-21 download/exploration
    phase per their README. So there is no real manifest format to point
    this at yet.

  - detection-team has no trained weights: detection-team/models/ only has
    a .gitkeep. There is no ball model to evaluate yet.

Given that, this script runs in two modes:

  1. REAL (partially): `--weights` takes any ultralytics-loadable weights
     path (a trained .pt, or a stock pretrained one). `--dataset` takes a
     real ultralytics-format `data.yaml` (images/ + labels/ dirs, YOLO-format
     label .txt files) if/when one exists. This is the same convention
     detection-team/configs/ball_yolo.example.yaml already assumes
     data-team will produce (it points at
     data-team/datasets/ball/data.yaml). That's an assumption, not a
     confirmed contract - data-team's README "Dataset schema" section is
     still blank, so re-check it once they fill it in.

  2. PLACEHOLDER (what actually runs today, with zero args): with no
     --weights, uses a stock pretrained YOLO model (COCO weights, same as
     scripts/quickstart.py) since no RoboCup-trained model exists yet.
     With no --dataset, builds a tiny synthetic dataset on the fly - a
     handful of generated images with a plain white circle drawn on them
     plus hand-written YOLO-format ground-truth boxes for COCO's "sports
     ball" class - so the whole pipeline (load weights -> run inference ->
     score against ground truth) is exercised end to end right now. This
     is CLEARLY placeholder data, not real ball images or real labels;
     swap `--dataset` for data-team's real split.py output and `--weights`
     for detection-team's real trained model as soon as those exist.

Also scaffolds (not fully built out - that's Week 6) a failure-case logger:
`find_failure_cases()` / `write_failure_log()` record which images produced
missed detections (false negatives) or false positives, so there's
somewhere for that data to go once we start testing on real unseen
footage.
"""

import argparse
import json
import sys
import tempfile
from dataclasses import asdict, dataclass, field
from pathlib import Path

import cv2
import numpy as np

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

DEFAULT_WEIGHTS = "yolov8n.pt"  # stock pretrained COCO weights - no RoboCup model exists yet


@dataclass
class EvalResult:
    """precision/recall/mAP, mirroring what detection-team's Oct milestone needs."""

    precision: float
    recall: float
    map50: float
    map50_95: float
    per_class: dict[str, dict[str, float]] = field(default_factory=dict)


def run_eval(
    weights: str | Path,
    data_yaml: str | Path,
    imgsz: int = 640,
    conf: float = 0.25,
    iou: float = 0.5,
    out_dir: str | Path | None = None,
) -> EvalResult:
    """Run detection metrics via ultralytics' built-in validator.

    This wraps `YOLO(weights).val(...)` rather than recomputing
    precision/recall/mAP by hand - ultralytics' validator already
    implements COCO-style AP correctly, and detection-team's eval.py will
    need the exact same computation, so there is only one place doing this
    math. See the module docstring's COORDINATION STATE for why this
    isn't importing anything from detection-team/training/eval.py (it's
    still a stub with nothing to import).
    """
    from ultralytics import YOLO

    model = YOLO(str(weights))
    run_dir = Path(out_dir) if out_dir else Path(tempfile.mkdtemp(prefix="eval_harness_"))
    metrics = model.val(
        data=str(data_yaml),
        imgsz=imgsz,
        conf=conf,
        iou=iou,
        verbose=False,
        plots=False,
        save_json=False,
        project=str(run_dir),
        name="val",
        exist_ok=True,
    )

    names = metrics.names
    per_class: dict[str, dict[str, float]] = {}
    for idx, class_id in enumerate(metrics.box.ap_class_index):
        per_class[names[int(class_id)]] = {
            "precision": float(metrics.box.p[idx]),
            "recall": float(metrics.box.r[idx]),
            "ap50": float(metrics.box.ap50[idx]),
            "ap50_95": float(metrics.box.maps[int(class_id)]),
        }

    return EvalResult(
        precision=float(metrics.box.mp),
        recall=float(metrics.box.mr),
        map50=float(metrics.box.map50),
        map50_95=float(metrics.box.map),
        per_class=per_class,
    )


def build_placeholder_dataset(out_dir: Path, weights: str | Path) -> Path:
    """Build a tiny, clearly-fake dataset so the harness runs end to end today.

    PLACEHOLDER DATA: a few generated images (plain background + a drawn
    white circle standing in for a ball) with hand-written YOLO-format
    ground-truth boxes. Not real TORSO-21 imagery, not a real annotation
    pipeline - swap for data-team's real split output once it exists (see
    module docstring).

    Ground truth is labeled with the pretrained model's own COCO "sports
    ball" class id (looked up from the loaded model rather than hardcoded,
    since it's a class in the stock weights, not our own shared.classes
    taxonomy). Once we're evaluating a RoboCup-trained model instead of
    the stock one, ground truth should use `shared.classes.BALL` /
    detection-team's own class indices instead.
    """
    from ultralytics import YOLO

    img_dir = out_dir / "images" / "val"
    lbl_dir = out_dir / "labels" / "val"
    img_dir.mkdir(parents=True, exist_ok=True)
    lbl_dir.mkdir(parents=True, exist_ok=True)

    names = YOLO(str(weights)).names
    name_to_id = {v: k for k, v in names.items()}
    ball_class_id = name_to_id.get("sports ball")
    if ball_class_id is None:
        raise SystemExit(
            "Placeholder dataset assumes a COCO-pretrained model with a "
            "'sports ball' class; pass --dataset explicitly for other weights."
        )

    width, height = 640, 480
    # (center_x, center_y, radius) - arbitrary, just needs to be a clean circle
    # placed away from image edges so the box stays fully in frame.
    circles = [(320, 240, 40), (150, 100, 25), (500, 350, 55)]

    for i, (cx, cy, r) in enumerate(circles):
        img = np.full((height, width, 3), (34, 139, 34), dtype=np.uint8)  # solid "field" green
        cv2.circle(img, (cx, cy), r, (255, 255, 255), -1)
        cv2.circle(img, (cx, cy), r, (0, 0, 0), 2)
        cv2.imwrite(str(img_dir / f"sample_{i:03d}.jpg"), img)

        x_min, y_min, x_max, y_max = cx - r, cy - r, cx + r, cy + r
        xc, yc = (x_min + x_max) / 2 / width, (y_min + y_max) / 2 / height
        bw, bh = (x_max - x_min) / width, (y_max - y_min) / height
        with (lbl_dir / f"sample_{i:03d}.txt").open("w") as f:
            f.write(f"{ball_class_id} {xc:.6f} {yc:.6f} {bw:.6f} {bh:.6f}\n")

    data_yaml = out_dir / "data.yaml"
    with data_yaml.open("w") as f:
        f.write(f"path: {out_dir}\n")
        f.write("train: images/val\n")  # no real train/val distinction - it's 3 images
        f.write("val: images/val\n")
        f.write("names:\n")
        for class_id, class_name in names.items():
            f.write(f"  {class_id}: {class_name}\n")

    return data_yaml


@dataclass
class FailureCase:
    """One missed detection or false positive, for Week 6 error analysis."""

    kind: str  # "missed_detection" or "false_positive"
    image: str
    class_name: str
    confidence: float | None  # None for missed detections (ground truth has no confidence)
    bbox_xyxy: list[float]


def find_failure_cases(
    weights: str | Path,
    data_yaml: str | Path,
    iou_thresh: float = 0.5,
    conf: float = 0.25,
) -> list[FailureCase]:
    """Scaffold for Week 6: log missed detections and false positives.

    NOT fully built out yet - this does simple greedy single-class IoU
    matching per image (each prediction matched to at most one unmatched
    ground-truth box of the same class, best IoU first). It doesn't handle
    trickier cases well (e.g. optimal one-to-one assignment across many
    overlapping boxes), which is fine for scaffolding now and worth
    revisiting once there's real unseen footage to run this against in
    Week 6.
    """
    import yaml
    from ultralytics import YOLO

    model = YOLO(str(weights))
    data_yaml = Path(data_yaml)
    data_cfg = yaml.safe_load(data_yaml.read_text())
    dataset_root = Path(data_cfg.get("path", data_yaml.parent))
    val_images_dir = dataset_root / data_cfg["val"]
    labels_dir = Path(str(val_images_dir).replace("images", "labels", 1))
    names = model.names

    failures: list[FailureCase] = []
    for image_path in sorted(val_images_dir.iterdir()):
        if image_path.suffix.lower() not in (".jpg", ".jpeg", ".png"):
            continue
        label_path = labels_dir / f"{image_path.stem}.txt"
        img = cv2.imread(str(image_path))
        height, width = img.shape[:2]

        gt_boxes = []
        if label_path.exists():
            for line in label_path.read_text().splitlines():
                cls_id, xc, yc, bw, bh = (float(v) for v in line.split())
                x_min = (xc - bw / 2) * width
                y_min = (yc - bh / 2) * height
                x_max = (xc + bw / 2) * width
                y_max = (yc + bh / 2) * height
                gt_boxes.append({"class_id": int(cls_id), "bbox": [x_min, y_min, x_max, y_max]})

        result = model.predict(source=str(image_path), conf=conf, verbose=False)[0]
        pred_boxes = [
            {
                "class_id": int(box.cls[0]),
                "confidence": float(box.conf[0]),
                "bbox": box.xyxy[0].tolist(),
            }
            for box in result.boxes
        ]

        matched_gt: set[int] = set()
        for pred in pred_boxes:
            best_iou, best_idx = 0.0, None
            for gt_idx, gt in enumerate(gt_boxes):
                if gt_idx in matched_gt or gt["class_id"] != pred["class_id"]:
                    continue
                iou = _iou(pred["bbox"], gt["bbox"])
                if iou > best_iou:
                    best_iou, best_idx = iou, gt_idx
            if best_idx is not None and best_iou >= iou_thresh:
                matched_gt.add(best_idx)
            else:
                failures.append(
                    FailureCase(
                        kind="false_positive",
                        image=str(image_path),
                        class_name=names.get(pred["class_id"], str(pred["class_id"])),
                        confidence=pred["confidence"],
                        bbox_xyxy=pred["bbox"],
                    )
                )

        for gt_idx, gt in enumerate(gt_boxes):
            if gt_idx not in matched_gt:
                failures.append(
                    FailureCase(
                        kind="missed_detection",
                        image=str(image_path),
                        class_name=names.get(gt["class_id"], str(gt["class_id"])),
                        confidence=None,
                        bbox_xyxy=gt["bbox"],
                    )
                )

    return failures


def _iou(box_a: list[float], box_b: list[float]) -> float:
    ax_min, ay_min, ax_max, ay_max = box_a
    bx_min, by_min, bx_max, by_max = box_b
    ix_min, iy_min = max(ax_min, bx_min), max(ay_min, by_min)
    ix_max, iy_max = min(ax_max, bx_max), min(ay_max, by_max)
    inter = max(0.0, ix_max - ix_min) * max(0.0, iy_max - iy_min)
    area_a = (ax_max - ax_min) * (ay_max - ay_min)
    area_b = (bx_max - bx_min) * (by_max - by_min)
    union = area_a + area_b - inter
    return inter / union if union > 0 else 0.0


def write_failure_log(failures: list[FailureCase], path: Path) -> None:
    with path.open("w") as f:
        for failure in failures:
            f.write(json.dumps(asdict(failure)) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--weights",
        type=str,
        default=DEFAULT_WEIGHTS,
        help="Path to trained weights, or a stock ultralytics model name. "
        f"Default: {DEFAULT_WEIGHTS} (PLACEHOLDER - no trained model exists yet).",
    )
    parser.add_argument(
        "--dataset",
        type=Path,
        default=None,
        help="Path to a real ultralytics-format data.yaml. If omitted, builds a "
        "PLACEHOLDER synthetic dataset instead (see module docstring).",
    )
    parser.add_argument("--imgsz", type=int, default=640)
    parser.add_argument("--conf", type=float, default=0.25)
    parser.add_argument("--iou", type=float, default=0.5)
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=None,
        help="Where to write run artifacts (placeholder dataset, ultralytics val "
        "output, failure log). Default: a fresh temp directory, printed at the end.",
    )
    parser.add_argument(
        "--skip-failure-log",
        action="store_true",
        help="Skip the Week 6 failure-case scaffold (it re-runs inference per image).",
    )
    args = parser.parse_args()

    out_dir = args.out_dir or Path(tempfile.mkdtemp(prefix="eval_harness_"))
    out_dir.mkdir(parents=True, exist_ok=True)

    is_placeholder_dataset = args.dataset is None
    if is_placeholder_dataset:
        print("No --dataset given: building a PLACEHOLDER synthetic dataset "
              f"(a few drawn-circle images, not real ball footage) under {out_dir}/dataset\n")
        data_yaml = build_placeholder_dataset(out_dir / "dataset", args.weights)
    else:
        data_yaml = args.dataset

    is_placeholder_weights = str(args.weights) == DEFAULT_WEIGHTS
    if is_placeholder_weights:
        print(f"No --weights given: using stock pretrained {DEFAULT_WEIGHTS} "
              "(PLACEHOLDER - not a RoboCup-trained model)\n")

    result = run_eval(
        args.weights, data_yaml, imgsz=args.imgsz, conf=args.conf, iou=args.iou, out_dir=out_dir / "val_run"
    )

    print("=" * 60)
    print("REAL RESULT computed by ultralytics.YOLO.val() against the given weights/dataset")
    print(f"({'PLACEHOLDER' if is_placeholder_dataset or is_placeholder_weights else 'real'} "
          f"inputs - see notes above)")
    print("=" * 60)
    print(f"precision (mean): {result.precision:.4f}")
    print(f"recall    (mean): {result.recall:.4f}")
    print(f"mAP50:            {result.map50:.4f}")
    print(f"mAP50-95:         {result.map50_95:.4f}")
    if result.per_class:
        print("\nper-class:")
        for class_name, m in result.per_class.items():
            print(
                f"  {class_name}: precision={m['precision']:.4f} recall={m['recall']:.4f} "
                f"ap50={m['ap50']:.4f} ap50-95={m['ap50_95']:.4f}"
            )

    if not args.skip_failure_log:
        failures = find_failure_cases(args.weights, data_yaml, iou_thresh=args.iou, conf=args.conf)
        failure_log_path = out_dir / "failure_log.jsonl"
        write_failure_log(failures, failure_log_path)
        print(f"\nWeek 6 failure-case scaffold: {len(failures)} failure(s) logged to {failure_log_path}")

    print(f"\nAll run artifacts under: {out_dir}")


if __name__ == "__main__":
    main()
