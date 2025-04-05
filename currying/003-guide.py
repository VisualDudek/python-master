# type: ignore

from functools import wraps
from typing import Callable, Any


def curry(func: Callable[..., Any]):
    @wraps(func)
    def curried(*args: Any):
        if len(args) >= func.__code__.co_argcount:
            return func(*args)
        return lambda *more_args: curried(*args, *more_args)

    return curried


@curry
def multipy(a, b, c):
    return a * b * c


# All at once
print(multipy(2, 3, 4))

# Step by step
print(multipy(2)(3)(4))
print(multipy(2, 3)(4))
print(multipy(2)(3, 4))
