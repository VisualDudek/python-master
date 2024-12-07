# monad boilerplate
# expect that bind func will return monad

from typing import Callable, Generic, TypeVar

# Type variables for input and output types
T = TypeVar("T")  # The type of the value contained in the monad
U = TypeVar("U")  # The type returned after applying a function


class Monad(Generic[T]):
    def __init__(self, value: T):
        self.value: T = value

    def bind(self, func: Callable[[T], "Monad[U]"]) -> "Monad[U]":
        """
        Chains a computation that takes a value of type T and
        returns a Monad wrapping a value of type U.
        """
        # vvvvvvvvvvvvvvvvvvvvv
        return func(self.value)

    def __repr__(self) -> str:
        return f"Monad({self.value})"

    # vvvvvvvvvvvvv it is just boilerplate to understand for other lang.
    # this is the same signature as `__init__`
    @staticmethod
    def unit(value: T) -> "Monad[T]":
        """
        Wraps a value of type T in a monad.
        """
        return Monad(value)


def add_one(x: int) -> int:
    return x + 1


def multipy_by_two(x: int) -> int:
    return x * 2


if __name__ == "__main__":

    monad = Monad(2)

    # Left identity
    # unit(x).bind(f) == f(x)
    #                 vvvvvvvvvvvvvvvvvvvvvvvvvv need lambda to ensure that you will return Monad[U]
    assert monad.bind(lambda x: Monad(add_one(x))).value == add_one(2)
