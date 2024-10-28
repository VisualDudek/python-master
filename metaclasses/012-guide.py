# very good example, simple ABC, focus on vvvvvvvvv
# TAKEAWYA: how abc.abstractmethod works under hood, just dunder __isabstractmethod__ attrib.
# if just prevents to create instance from class that do not implement abstractmethods


def abstractmethod(f):
    f.__isabstract__ = True
    return f


def abstractmethods(cls):
    seen = set()
    abstract = []
    while isinstance(cls, ABCMeta):
        for key, val in vars(cls).items():
            if key in seen:
                continue
            seen.add(key)
            if getattr(val, "__isabstract__", False):
                abstract.append(key)
        # object is not ABCMeta so mro will have at least 2 entries
        cls = cls.__mro__[1]
    return abstract


# vvvvvvvvvvvvvvvvvvvvvvv
class ABCMeta(type):
    def __call__(abccls, *args, **kwargs):  # called when you -> A()
        print("call", abccls, args, kwargs)
        abstract = abstractmethods(abccls)
        if abstract:
            raise TypeError("no implementation for: " + ", ".join(abstract))
        return super().__call__(*args, **kwargs)


class ABC(metaclass=ABCMeta):
    pass


# vvvvvvvv by default you inherit from ABC and mark some function with abstract method
class A(ABC):
    def __init__(self, *args, **kwargs):
        print("init", self, args, kwargs)

    @abstractmethod
    def f(self):
        pass

    @abstractmethod
    def g(self):
        pass


# vvvvvvv here I pretend that I have implementation of abstract method
class B(A):
    def f(self):
        pass

    def g(self):
        pass


# vvvvvvvvvvvvvvv
try:
    A()
except TypeError as e:
    print(e)

print(f"{type(B())=}")
print(f"{type(B)=}")
