# Python 3.12 improved syntax
# mypy may not be ready
from typing import Protocol, TypeVar

# will not need this anymore
# T = TypeVar("T", bound=int | float)


class Adder(Protocol):  # generic Protocol[T] is also OUT
    def add[T: int | float](self, x: T, y: T) -> T: ...


class IntAdder:
    def add(self, x: int, y: int) -> int:
        return x + y


class FloatAdder:
    def add(self, x: float, y: float) -> float:
        return x + y


def add(adder: Adder) -> None:
    print(adder.add(2, 3))


add(IntAdder())
