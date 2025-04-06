# overriding magic methods, e.g. add two vectors
from typing import NamedTuple


class Vector(NamedTuple):
    x: int
    y: int

    # fmt: off
    def __add__(self, other: 'Vector') -> 'Vector': # type: ignore[override]
        return Vector(self.x + other.x, self.y + other.y)


# fmt: on

v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1 + v2)  # Vector(x=4, y=6)
