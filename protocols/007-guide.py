# issues while using type hints with Protocols
from typing import Protocol


class Adder(Protocol):
    def add(
        self, x: float, y: float
    ): ...  # implements .add() method, which defines the Adder protocol itselft


class IntAdder:
    def add(self, x, y):  # PROBLEM: static checker will consider methods args and
        # return value as of type Any, which makes type check succeed, OUCH!
        return x + y


def add(adder: Adder) -> None:
    print(adder.add(2, 3))  # One big change: IDE now support autocopletion


add(IntAdder())  # will be OK in run-time and mypy also will be ok, OUCH!
