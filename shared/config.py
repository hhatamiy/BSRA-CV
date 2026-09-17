"""Common YAML config loading used across subteams.

Training configs (detection-team/configs/), calibration configs
(integration-team/calibration/), and benchmark configs
(testing-deployment-team/benchmarks/) can all load through this so there
is one place that defines how config files are found and parsed.
"""

from pathlib import Path
from typing import Any

import yaml


def load_config(path: str | Path) -> dict[str, Any]:
    path = Path(path)
    with path.open("r") as f:
        return yaml.safe_load(f)
