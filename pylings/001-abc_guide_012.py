# 1. Import necessary modules and define the Shape protocol here
# Import the necessary module for creating a protocol

from math import pi

# Define the Shape protocol here (HINT: Use the typing module)


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


# 2. Modify the describe_shape_better function to accept objects that match the Shape protocol
def describe_shape_better(shape) -> None:
    # Ensure that shape is a type that follows the Shape protocol
    print(f"{type(shape).__name__}")
    print(f" Area: {shape.area():.2f}")
    print(f" Perimeter: {shape.perimeter():.2f}")
