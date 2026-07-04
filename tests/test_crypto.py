from vaultutils.crypto import new_key, seal, open_sealed


def test_roundtrip():
    k = new_key()
    assert open_sealed(k, seal(k, "hello")) == "hello"
