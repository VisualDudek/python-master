# basic example of a functor

from typing import Any, Callable


class Functor:
    def __init__(self, value: Any) -> None:
        self.value = value

    def map(self, func: Callable[[Any], Any]) -> "Functor":
        return Functor(func(self.value))


def add_one(x: int) -> int:
    return x + 1


def multiply_by_two(x: int):
    return x * 2


if __name__ == "__main__":

    f = Functor(2)

    g = f.map(add_one)

    assert isinstance(g, Functor)

    assert f.map(add_one).map(multiply_by_two).value == 6

    # composition
    assert (
        f.map(add_one).map(multiply_by_two).value
        == f.map(lambda x: multiply_by_two(add_one(x))).value
    )
