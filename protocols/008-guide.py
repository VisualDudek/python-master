# one way to SOLVE issue from prev. file is to
# add type hints to class that implements Adder protocol
from typing import Protocol


class Adder(Protocol):
    def add(
        self, x: float, y: float
    ): ...  # implements .add() method, which defines the Adder protocol itselft


class IntAdder:
    def add(self, x: int, y: int) -> int:  # SOLUTION
        return x + y


def add(adder: Adder) -> None:
    print(adder.add(2, 3))


add(IntAdder())  # mypy now correct panic about incompatible type

# What if we want protocol Adder to accept int and float?
