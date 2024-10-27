# Another angle to explain metaclasses
# see example with overloaded class methods
# see next file for partial solution using overload from typing module


class A:
    def f(self, x: int):
        print("A.f int overload", self, x)

    def f(self, x: str):
        print("A.f str overload", self, x)

    def f(self, x, y):
        print("A.f two arg overload", self, x, y)


a = A()

try:
    a.f(1)
except TypeError:
    print(
        """
          Calling `a.f(1)` will raise TypeError
          A.f() missing 1 required positional argument: 'y'
          BC:
          each f class method definition overrides previos
          thus class A has only one f with signature (self, x, y)
          """
    )
