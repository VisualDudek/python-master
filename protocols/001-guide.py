# when duck typing can be an issue
from typing import Union


def add(a: Union[float, int], b: Union[float, int]) -> float:
    return float(a + b)


# PEP 604 Allow writing Union[X, Y] as X | Y

print(add(2, 4))  # OUTPUT: 6.0

print(add("2", "4"))  # OUTPUT: 24.0
# Will no panic at runtume, instead it will cat two stings,
# this is PROBLEM that can be solved by static type checking
# e.g. mypy
