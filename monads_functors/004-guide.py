# monad Maybe usecase

from __future__ import annotations
from typing import Generic, Optional, Callable, TypeVar

T = TypeVar("T")
U = TypeVar("U")


class Maybe(Generic[T]):
    def __init__(self, value: Optional[T]) -> None:
        self.value = value

    def bind(self, func: Callable[[T], Maybe[U]]) -> Maybe[T] | Maybe[U]:
        return self if self.value is None else func(self.value)

    __match_args__ = ("value",)

    def __match__(self, other: Maybe[T]) -> bool:
        return self.value == other.value


# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# this translate python exeption error handling into monadic error handling model
def parse_int(value: str) -> Maybe[int]:
    try:
        return Maybe(int(value))
    except ValueError:
        return Maybe(None)


def is_positive(value: int) -> Maybe[int]:
    return Maybe(value) if value > 0 else Maybe(None)


# vvvvvvvvvvvvvvvvvvvvvvvvvvv
# does not return monad BUT you can use lambda in bind method to wrap result into monad
def double(value: int) -> int:
    return 2 * value


def validate_and_process(input_str: str) -> Maybe[str] | Maybe[int]:
    # vvvvvvvvvvvvvvvvvvvv
    # ??? you can put each method call in seperate line ???
    return (
        Maybe(input_str)
        .bind(parse_int)
        .bind(is_positive)
        .bind(lambda n: Maybe(double(n)))
    )


def main() -> None:

    inputs = ["5", "-3", "foo"]

    for input_str in inputs:
        result = validate_and_process(input_str)
        match result:
            case Maybe(None):
                print(f"Invalid input: {input_str}")
            case Maybe(value=int()):
                print(f"Result: {result.value}")
            case _:
                print("Unespected input!")


if __name__ == "__main__":
    main()
