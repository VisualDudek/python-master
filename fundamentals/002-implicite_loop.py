# Implement `for_each` without using `for` or `while` keywords
# Tail Call Optimization is not natively supported in Python
# ^^^^^^^^^^^^^^^^^^^^^^--- calling function without placing another
# function call on the stack.
from typing import Any, Callable


# def for_each(lst: list[Any], func: Callable[[Any], None]) -> None:
#     pass


# Example usage:
# for_each(["kot", "pies", "mysz"], print)
# Output:
# kot
# pies
# mysz

# Recursion implementation

lst = ["kot", "pies", "mysz"]


def for_each(lst: list[Any], func: Callable[[Any], None], index: int = 0) -> None:
    if index < len(lst):
        func(lst[index])
        for_each(lst, func, index + 1)


for_each(lst, print)

# Conditions for Tail Call Optimization
# 1. The recursive call must be the last operation in the function. This is called a tail call.
# 2. No additional computation should follow the recursive call,
# as any further operations would require the current stack frame to be retained.
