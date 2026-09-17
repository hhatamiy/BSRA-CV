# shared/

Code that every subteam depends on, so it lives in one place instead of
being copy-pasted or drifting out of sync.

- `classes.py` — canonical object class names/IDs (ball, robot, goalpost,
  field_line, landmark). Detection, data-team labeling, and integration
  should all import class names from here.
- `types.py` — shared dataclasses: `Detection` (detection-team's output,
  in image space) and `PerceptionObject` (integration-team's output,
  robot-relative position). See [ARCHITECTURE.md](../ARCHITECTURE.md) for
  where each type sits in the pipeline.
- `config.py` — common YAML config loading used by training, calibration,
  and benchmark configs.

If you need something another subteam would also want, it probably
belongs here rather than in your subteam folder.
