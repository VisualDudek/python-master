# learn staticmethod vs. classmethod

# Does @classmethod is only sugar syntax and you can reach cls using dunder methods?
# yep seems so


class A:
    @classmethod
    def method_class(cls, x):
        print(f"method_class({cls=}, {x=})")

    def method(self, x):
        print(f"method({self.__class__=}, {x=})")


a = A()
a.method_class(2)
a.method(1)
