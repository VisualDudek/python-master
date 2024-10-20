# follow up from prev. file
# TAKEAWAY: you can check type annotation in runtime via. `__annotations__`

from typing import Protocol, runtime_checkable


@runtime_checkable
class Indexable(Protocol):
    def __index__(self) -> int: ...


class A:
    def __index__(self) -> float:
        return 3.14


a = A()
assert isinstance(a, Indexable) == True  # OUCH! will comfort in runtime

# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
print(f"{a.__index__.__annotations__=}")
print(f"{Indexable.__index__.__annotations__=}")

assert a.__index__.__annotations__ != Indexable.__index__.__annotations__
