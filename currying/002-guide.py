from functools import partial


def mypower(base: int, exponent: int):
    return base**exponent


square = partial(mypower, exponent=2)

print(square(5))  # Output: 25
