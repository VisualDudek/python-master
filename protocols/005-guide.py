# inheritance OUT, structural subtyping IN
# example of Dog and Cat class without a formal relationship
# BUT inplicit implemnt the same public interface -> they have
# tha same internal structure, including methods and attributes.
# They are STRUCTURAL SUBTYPES -> can use duck typing context.
# BUT in such inexplicite interface implementation there is a PROBLEM
class Dog:
    def __init__(self, name) -> None:
        self.name = name

    def make_sound(self):
        print(f"{self.name} is barking.")

    def eat(self):
        print(f"{self.name} is eating.")

    def drink(self):
        print(f"{self.name} is drinking.")


class Cat:
    def __init__(self, name) -> None:
        self.name = name

    def make_sound(self):
        print(f"{self.name} is meowing.")

    def eat(self):
        print(f"{self.name} is eating.")

    def drink(self):
        print(f"{self.name} is drinking.")


for animal in [Cat("Tom"), Dog("Pluto")]:
    animal.eat()  # it works in runtime BUT
    animal.drink()  # PROBLEM mypy and IDE do not know that animal has .eat() method
    animal.make_sound()
