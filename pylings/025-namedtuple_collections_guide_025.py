# add property: area
from typing import NamedTuple


class Rectangle(NamedTuple):
    w: float
    h: float

    # WRITE YOUR CODE HERE


# Usage
rect = Rectangle(5, 4)
print(rect.area)  # prints 20
