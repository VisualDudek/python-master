# great example how to use __init_subclass__ to register classes
# TAKEAWAY: `super().__init_subclass__(**kwargs)` in EncryptedFile class ensures that if
# there are any other base classes that also implement `__init_subclass__`, their implementation
# are properly called.

from typing import Dict, Callable
import codecs
import itertools


class EncryptedFile:  # DO NOT USE ANY OF THESE FOR REAL ENCRYPTION
    _registry: Dict[str, Callable] = {}  # 'rot13' -> ROT13Text

    def __init_subclass__(cls, prefix, **kwargs):
        super().__init_subclass__(**kwargs)  # <-------
        cls._registry[prefix] = cls

    def __new__(cls, path: str, key=None):
        prefix, sep, suffix = path.partition(":///")
        if sep:
            file = suffix
        else:
            file = prefix
            prefix = "file"
        subclass = cls._registry[prefix]
        obj = object.__new__(subclass)  # <------ not calling super().__new__
        obj.file = file
        obj.key = key
        return obj

    def read(self) -> str:
        raise NotImplementedError


class Plaintext(EncryptedFile, prefix="file"):
    def read(self):
        # with open(self.file, "r") as f:
        # return f.read()
        text = "hello world"
        return text


class ROT13Text(EncryptedFile, prefix="rot13"):
    def read(self):
        # with open(self.file, "r") as f:
        #     text = f.read()
        text = "uryyb jbeyq"
        return codecs.decode(text, "rot_13")


class OneTimePadXorText(EncryptedFile, prefix="otp"):
    def __init__(self, path, key):
        if isinstance(self.key, str):
            self.key = self.key.encode()

    def xor_bytes_with_key(self, b: bytes) -> bytes:
        return bytes(b1 ^ b2 for b1, b2 in zip(b, itertools.cycle(self.key)))

    def read(self):
        # with open(self.file, "rb") as f:
        #     btext = f.read()
        text_input = "BGQGR@ZVTG[_P[U[]S"
        btext = text_input.encode("utf-8")
        text = self.xor_bytes_with_key(btext).decode()
        return text


print("ENCRYPTED FILE EXAMPLE")
print(EncryptedFile("plaintext_hello.txt").read())
print(EncryptedFile("rot13:///rot13_hello.txt").read())
print(EncryptedFile("otp:///otp_hello.txt", key="1234").read())
