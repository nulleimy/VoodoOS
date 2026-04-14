from pathlib import Path
from typing import Any, Dict

import yaml


class ConfigLoader:
    def load_yaml(self, path: str) -> Dict[str, Any]:
        file_path = Path(path)
        if not file_path.exists():
            raise FileNotFoundError(f"Config file not found: {path}")

        with file_path.open("r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle) or {}

        if not isinstance(data, dict):
            raise ValueError(f"Expected dict-like YAML content in: {path}")

        return data
