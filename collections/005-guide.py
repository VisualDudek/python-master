from typing import NamedTuple


class Rectangle(NamedTuple):
    w: float
    h: float

    @property
    def area(self) -> float:
        return self.w * self.h


# Usage

rect = Rectangle(5, 4)
print(rect.area)  # prints 20
