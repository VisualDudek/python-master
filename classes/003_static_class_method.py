# learn staticmethod vs. classmethod

# implementation of staticmethod and classmethod using descriptor protocol


class StaticMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        return self.func


class ClassMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        return self.func.__get__(owner, type(owner))
