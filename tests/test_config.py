from vaultutils.config import load_config, require
import tempfile, os


def test_load(tmp_path):
    p = tmp_path / ".env"
    p.write_text("A=1\n# c\nB = two\n")
    cfg = load_config(str(p))
    assert cfg == {"A": "1", "B": "two"}


def test_require(tmp_path):
    try:
        require({"A": "1"}, "A", "B")
        assert False
    except KeyError:
        pass
