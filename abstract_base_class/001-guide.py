# Understanding Virtual Subclass, start from regular subclass and check how
# isinstance() and issubclass() behaves

from abc import ABC, abstractmethod


# Define an abstract base class (ABC)
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


# Define a concrete subclass that inherits from Animal
class Dog(Animal):
    def make_sound(self):
        return "Woof!"


dog = Dog()

# This works because Dog inherits from Animal
print(isinstance(dog, Animal))  # Output: True
print(issubclass(Dog, Animal))  # Output: True
assert isinstance(dog, Animal) == True
