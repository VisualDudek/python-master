# follow up from prev. file
# example where you wnat to create your own protocol
# When you have Circle, Square and Rectangle and fn that oparates on those classes
# it is convinient to "wrap" them into Shape type -> here protocol comes in

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


# ----------------vvvvvvvv accepts any obj. NOT GOOD
def describe_shape(shape):
    print(f"{type(shape).__name__}")
    print(f" Area: {shape.area():.2f}")
    print(f" Perimeter: {shape.perimeter():.2f}")


# SOLUTION
from typing import Protocol


class Shape(Protocol):
    def area(self) -> float: ...

    def perimeter(self) -> float: ...


def describe_shape_better(shape: Shape) -> None:
    print(f"{type(shape).__name__}")
    print(f" Area: {shape.area():.2f}")
    print(f" Perimeter: {shape.perimeter():.2f}")
