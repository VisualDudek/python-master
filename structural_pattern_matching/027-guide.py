# **mind bending** Structual Pattern Matching works well also with **structural subtypes** (not only with nominal subtypes).
# TAKEAWAY: type annotation is crazy here, check override and UnnecessaryComparison

from typing import NamedTuple, Protocol, runtime_checkable


@runtime_checkable
class Additive(Protocol):
    def __add__(self, other: "Additive"): ...


class Vector(NamedTuple):
    x: int
    y: int

    def __add__(self, other: "Vector") -> "Vector":  # type: ignore[override]
        return Vector(self.x + other.x, self.y + other.y)


# pyright: reportUnnecessaryComparison=false
match Vector(3, 4):
    case Additive():
        print("Matched an additive object.")
    case _:
        pass
