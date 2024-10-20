# How to check types explicitly?
# 1. you can use built-in `isinstance()` to check whether an object
# comes from a given class.
# 2. To check whether an object has a specific method or attribute,
# you can use the built-in `hasattr()`


class Duck:
    def fly(self):
        print("The duck is flying")

    def swim(self):
        print("The duck is swimming")


class Pigeon:
    def fly(self):
        print("The pigeon is flying")


birds = [Duck(), Pigeon()]

# POC: vvvvvvvvvv
# two legacy ways to check if obj has swim method before calling it

for bird in birds:
    if isinstance(bird, Duck):
        bird.swim()


for bird in birds:
    if hasattr(bird, "swim"):
        bird.swim()
