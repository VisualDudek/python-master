# trying to fix proble from prev. file
# using typing.overloaded decorator
# TAKEAWYA: can overload only signature that differs in types, cannot overload f(x) with f(x,y)
# ^^^^^ can use metaclasses to do this
#                                                              ^^^^^^ OUCH !!! see next file
# TAKEAWAY: use `get_overloads()` to introspect overloded fn. at runtime

from typing import overload, get_overloads, Union


class A:
    @overload
    def f(self, x: None) -> None: ...

    @overload
    def f(self, x: int) -> int: ...

    @overload
    def f(self, x: str) -> str: ...

    # NOT TRUE, see next file
    # vvvvvvvvvvvvvvvv cannot be done using overloaded BUT can be done using metaclasses
    # @overload
    # def f(self, x: int, y:str) -> tuple[int, str]: ...

    def f(self, x: Union[None, int, str]):
        if isinstance(x, int):
            return ("A.f int overload", self, x)
        elif isinstance(x, str):
            return ("A.f str overload", self, x)


a = A()

print(f"{a.f(1)=}")
print(f"{a.f("A")=}")

# vvvvvvvvv overloaded funcs introspected at runtime
print(f"\n {get_overloads(a.f)=}")

for fn in get_overloads(a.f):
    print(fn.__annotations__)
