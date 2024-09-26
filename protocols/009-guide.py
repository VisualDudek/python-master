# What if we want protocol Adder to accept int and float?
# maybe you have an idea for SOLUTION -> union type hints, OUCH!!!
from typing import Protocol


class Adder(Protocol):
    def add(
        self, x: float | int, y: float | int
    ) -> float | int: ...  # ^^^^^^^^^^^^^^^^ update to accept either integer or float


class IntAdder:
    def add(self, x: int, y: int) -> int:
        return x + y


def add(adder: Adder) -> None:
    print(adder.add(2, 3))


add(IntAdder())  # wont work bc. Adder prtocol expect Union[int, float] not just int

# seek help in generic Protocols
