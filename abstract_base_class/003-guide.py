# Understanding Virtual Subclass, practical example
# POC: you have third-party class AND you want to threat it
# as a Shape in our application

from abc import ABC, abstractmethod


# Define an abstract base class for shapes
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


# Circle explicitly inherits from Shape
# Regular Subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2


circle = Circle(5)
print(isinstance(circle, Shape))  # Output: True


# POC:
# Third-party class that doesn't inherit from Shape
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Register Rectangle as a virtual subclass of Shape
Shape.register(Rectangle)

rectangle = Rectangle(4, 5)
assert isinstance(rectangle, Shape) == True
