import os
from typing import Dict


def load_config(path: str = ".env") -> Dict[str, str]:
    """Parse a dotenv-style file into a dict. Comments and blanks ignored."""
    cfg: Dict[str, str] = {}
    if not os.path.exists(path):
        return cfg
    with open(path, encoding="utf-8") as fh:
        for raw in fh:
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, val = line.split("=", 1)
            cfg[key.strip()] = val.strip().strip('"').strip("'")
    return cfg


def require(cfg: Dict[str, str], *keys: str) -> None:
    missing = [k for k in keys if k not in cfg]
    if missing:
        raise KeyError(f"missing config keys: {', '.join(missing)}")
