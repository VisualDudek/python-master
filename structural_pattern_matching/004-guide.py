# avoid using pattern mataching as `switch` statement replacement
# Use jump tabel, which you can use to implement dynamic dispatch
# TAKEAWAY: lambda in .get is genius

from operator import add, sub, mul, truediv as div


def apply(operator, left, right):
    return {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div,
    }.get(
        operator, lambda *args: None
    )(left, right)
