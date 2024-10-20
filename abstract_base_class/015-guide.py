# follow up from prev. file
# TAKEAWAY: runtime_checkable and isinstance() check only names attributes
# it does not check type signatures
# SOLUTION in next file

from typing import Protocol, runtime_checkable


@runtime_checkable
class Indexable(Protocol):
    def __index__(self) -> int: ...


# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv match name attributes BUT fail at type
# siganture on return type -> int != float
class A:
    def __index__(self) -> float:
        return 3.14


a = A()
assert isinstance(a, Indexable) == True  # OUCH! will comfort in runtime

b: Indexable = A()  # <--- this is only happening in type checking time
