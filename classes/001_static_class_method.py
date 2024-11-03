# learn staticmethod vs. classmethod


# Starting point: three kind of methods in class
# TAKEAWAY: keep in mind signature of each function
# classmethod can be:
# - Alternative Constructor
# - Managing Class-Level Data
# - Implement Factory Method <- diff from alternative constructor


class A:
    def method(self, x):
        print(f"method({self=}, {x=})")

    @classmethod
    def method_class(cls, x):
        print(f"method_class({cls=}, {x=})")

    @staticmethod
    def method_static(x):
        print(f"method_static({x=})")


a = A()
a.method(1)
a.method_class(2)  # TAKEAWAY: you can access class obj.
a.method_static(3)
