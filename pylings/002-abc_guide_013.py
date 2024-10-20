# This exercise aims to teach you about runtime checking of protocols in Python.
from typing import Protocol, Any

# 1. Import necessary decorator


class Shape(Protocol):
    def area(self) -> float: ...

    def perimeter(self) -> float: ...


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


def describe_shape(shape: Shape) -> None:
    print(f"{type(shape).__name__}")
    print(f" Area: {shape.area():.2f}")
    print(f" Perimeter: {shape.perimeter():.2f}")


# 2. Check if obj implements the Shape protocol
def verify_is_Shape(obj: Any) -> bool:  # type: ignore
    pass


# Test cases
assert verify_is_Shape(Rectangle(2, 4)) == True
assert verify_is_Shape(42) == False
