# implement fn: apply as jump table

from operator import add, sub, mul, truediv as div


def apply(operator, left, right):
    return {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div,
    }.get(
        operator,
        lambda *args: None,
    )(left, right)


def f(*_) -> None:
    return None


def apply_easier_to_read(operator, left, right):
    return {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div,
    }.get(
        operator,
        f,
    )(left, right)


assert apply("+", 2, 2) == 4
assert apply("**", 2, 2) is None

assert apply_easier_to_read("+", 2, 2) == 4
assert apply_easier_to_read("**", 2, 2) is None
