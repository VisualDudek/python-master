# example of (explicite) formal protocol
# ellipsis (...) syntax
# IntAdder and FloatAdder DO NOT inherit from Adder portocol
# will get to typhints in next file
from typing import Protocol


class Adder(Protocol):
    def add(
        self, x, y
    ): ...  # implements .add() method, which defines the Adder protocol itselft


class IntAdder:
    def add(self, x, y):
        return x + y


class FloatAdder:
    def add(self, x, y):
        return x + y


def add(adder: Adder) -> None:
    print(adder.add(2, 3))  # One big change: IDE now support autocopletion


add(IntAdder())  # and mypy do not raise issue
add(FloatAdder())
