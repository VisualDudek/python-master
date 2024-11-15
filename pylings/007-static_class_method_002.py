# what is the other method to get class object from instance?


class A:
    def method(self, x):
        return (self, x)  # <------------

    @classmethod
    def method_class(cls, x):
        return (cls, x)


a = A()

assert a.method(1) == a.method_class(1), f"{a.method(1)=} != {a.method_class(1)=}"
