import secrets
from typing import Dict


class Rotator:
    """Rotate named credentials in a config dict."""

    def __init__(self, cfg: Dict[str, str]):
        self.cfg = cfg

    def _fresh(self, nbytes: int = 24) -> str:
        return secrets.token_urlsafe(nbytes)

    def rotate(self, name: str) -> str:
        key = f"{name.upper()}_SECRET"
        self.cfg[key] = self._fresh()
        return self.cfg[key]
