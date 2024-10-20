# follow up from prev. file
# example `@runtime_checkable`
# TAKEAWAY Mind shift: Protocols have no use at runtime -> if you want to use
# `isinstace()` or `issubclass()` against protocol you need to make it runtime_checkable

from math import pi


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return pi * self.radius**2

    def perimeter(self) -> float:
        return 2 * pi * self.radius


class Square:
    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side**2

    def perimeter(self) -> float:
        return 4 * self.side


class Rectangle:
    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width

    def perimeter(self) -> float:
        return 2 * (self.length + self.width)


from typing import Protocol
from typing import runtime_checkable


# vvvvvvvvvvvvvvvv
@runtime_checkable
class Shape(Protocol):
    def area(self) -> float: ...

    def perimeter(self) -> float: ...


def describe_shape(shape: Shape) -> None:
    print(f"{type(shape).__name__}")
    print(f" Area: {shape.area():.2f}")
    print(f" Perimeter: {shape.perimeter():.2f}")
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    assert isinstance(shape, Shape) == True


describe_shape(Rectangle(2, 2))
