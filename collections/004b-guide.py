# overriding magic methods, e.g. add two vectors
# use @overload decorator to fix type hint AND
# enable adding scalar to Vector
# AND
# enable postponed evaluation

from __future__ import annotations
from typing import NamedTuple, overload, Union


class Vector(NamedTuple):
    x: int
    y: int

    # Only type hints for diff overloads
    @overload
    def __add__(self, other: Vector) -> Vector: ...

    @overload
    def __add__(self, other: int) -> Vector: ...

    # Actual implementation (no @overload decorator)
    def __add__(self, other: Vector | int) -> Vector: 
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        elif isinstance(other, int):
            return Vector(self.x + other, self.y + other)
        return NotImplemented



# fmt: on

v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1 + v2)  # Vector(x=4, y=6)
print(v1 + 5)  # Vector(x=6, y=7)
