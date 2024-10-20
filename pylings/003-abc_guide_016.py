# This exercise aims to teach you about __annotations__
from typing import Protocol, runtime_checkable


@runtime_checkable
class Indexable(Protocol):
    def __index__(self) -> int: ...


class A:
    def __index__(self) -> float:
        return 3.14


a = A()
assert isinstance(a, Indexable) == True  # OUCH! will comfort in runtime

# 1. Write assertion that will seve you from above false positive, wrong return types
assert xxxx != xxxx
