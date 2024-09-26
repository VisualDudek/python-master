# nominal subtyping example
# You can use Dog or Cat instance when Animal instance is expected.
# POC: use builtin isinstance() <- explicit type checking
class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def dring(self):
        print(f"{self.name} is drinking.")


class Dog(Animal):  # nominal subtype of Animal
    def bark(self):
        print(f"{self.name} is barking.")


class Cat(Animal):  # nominal subtype of Animal
    def meow(self):
        print(f"{self.name} is meowing.")


pluto = Dog("Pluto")
tom = Cat("Tom")

print(f"{isinstance(pluto, Animal)=}")
print(f"{isinstance(pluto, Dog)=}")
print(f"{isinstance(tom, Animal)=}")
print(f"{isinstance(tom, Cat)=}")
