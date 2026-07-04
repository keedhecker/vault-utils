# vaultutils

Small utilities for loading configuration, rotating credentials, and light symmetric crypto.
Used internally across our services.

## Install
```bash
pip install -e .
```

## Quickstart
```python
from vaultutils import load_config, Rotator
cfg = load_config(".env")
Rotator(cfg).rotate("db")
```
See `docs/` for details.
