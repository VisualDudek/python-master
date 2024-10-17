# Understanding Virtual Subclass, start from regular subclass and check how
# isinstance() and issubclass() behaves
# add Cat virtual subclass thant do not inherit from Animal BUT behaves like subclass of Animal
# Cat do not receive any methods or arrtibutes from Animal
# Cat becomes virtual subclass of Animal when it is register! not at definition level.

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


# DO NOT INHERIT FROM ANIMAL
class Cat:
    def make_soud(self):
        return "Meow!"


# Register Cat as a virtual subclass of Animal
Animal.register(Cat)

cat = Cat()

# Now Cat behaves like a subclass of Animal for isinstance and issubclass
assert isinstance(cat, Animal) == True
assert issubclass(Cat, Animal) == True
