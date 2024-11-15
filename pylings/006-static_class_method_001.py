# what are signatures for each methods?


class A:
    def method(...):
        print(f"method({}, {})")

    @classmethod
    def method_class(...):
        print(f"method_class({}, {})")

    @staticmethod
    def method_static(...):
        print(f"method_static({})")


a = A()
a.method(1)
a.method_class(2)
a.method_static(3)