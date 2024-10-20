# Keep in mind what is happening only in type checking time
# and NOT IN RUNTIME
# example:
# TAKEAWAY: your custom Indexable protocol is equvalent to collections.abc.[Container | Hashable | ...]

from typing import Protocol


class Indexable(Protocol):
    def __index__(self) -> int: ...


class A:
    def __index__(self) -> int:
        return 2


a: Indexable = A()  # <--- this is only happening in type checking time
