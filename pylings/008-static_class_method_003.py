# implement staticmethod usig class decirator and descriptor protocol


class StaticMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, instnce, owner):
        return self.func


class A:
    def method(x):
        return x

    @StaticMethod
    def method_static(x):
        return x


a = A()
print(A)
print(a)
print(a.method())
print(a.method_static(1))
