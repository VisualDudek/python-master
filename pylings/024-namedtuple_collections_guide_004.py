# overriding magic methods
# enable adding two vectors
from typing import NamedTuple


class Vector(NamedTuple):
    x: int
    y: int

    # fmt: off
    # WRITE YOUR CODE HERE


# fmt: on

v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1 + v2)  # Vector(x=4, y=6)
