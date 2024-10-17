# Example to highlight the difference between Interface and Contract

from abc import ABC, abstractmethod


# Interface
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Contract
class Rectangle:
    def __init__(self, width, height):
        assert width > 0 and height > 0, "Dimensions must be positive"
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def resize(self, new_width, new_height):
        # Preconditions: new dimensions must be positive
        assert new_width > 0 and new_height > 0, "New dimensions must be positive"

        self.width = new_width
        self.height = new_height

        # Postcondition: width and height must be updated correctly
        assert self.width == new_width and self.height == new_height
