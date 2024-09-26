# generic Protocols will save you
# new syntax: 'T = TypeVar("T")'
from typing import Protocol, TypeVar


T = TypeVar("T", bound=int | float)  # define generic type bound to only int or float


class Adder(Protocol[T]):  # generic protocol
    def add(self, x: T, y: T) -> T: ...


class IntAdder:
    def add(self, x: int, y: int) -> int:
        return x + y


class FloatAdder:
    def add(self, x: float, y: float) -> float:
        return x + y


def add(adder: Adder) -> None:
    print(adder.add(2, 3))


add(IntAdder())

# in Python 3.12 syntax is even better