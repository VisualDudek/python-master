# trying to @overload different type signatures
# it turns out that it can be done but with kind of hack of using default values

from typing import overload, get_overloads, Union


class A:
    @overload
    def f(self, x: int) -> int: ...

    @overload
    def f(self, x: str) -> str: ...

    @overload
    def f(self, x: int, y: str) -> tuple[int, str]: ...

    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv   vvvvv this is the hack !!!
    def f(self, x: Union[None, int, str], y: str = "A"):
        if isinstance(x, int):
            return ("A.f int overload", self, x)
        elif isinstance(x, str):
            return ("A.f str overload", self, x)


a = A()

print(f"{a.f(1)=}")
print(f"{a.f("A")=}")

print(f"\n {get_overloads(a.f)=}")

for fn in get_overloads(a.f):
    print(fn.__annotations__)
