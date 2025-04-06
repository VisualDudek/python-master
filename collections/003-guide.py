# subclassing NamedTuple and adding methods

from typing import NamedTuple


class Point(NamedTuple):
    x: float
    y: float

    def distance_to_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5


# Usage
p = Point(3, 4)
print(p)  # Point(x=3, x=4)
print(p.distance_to_origin())  # 5.0
