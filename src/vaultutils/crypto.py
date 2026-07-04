import base64
from cryptography.fernet import Fernet


def new_key() -> str:
    return Fernet.generate_key().decode()


def seal(key: str, plaintext: str) -> str:
    token = Fernet(key.encode()).encrypt(plaintext.encode())
    return base64.urlsafe_b64encode(token).decode()


def open_sealed(key: str, blob: str) -> str:
    token = base64.urlsafe_b64decode(blob.encode())
    return Fernet(key.encode()).decrypt(token).decode()
