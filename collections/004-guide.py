# overriding magic methods, e.g. add two vectors
from typing import NamedTuple


class Vector(NamedTuple):
    x: int
    y: int

    # fmt: off
    def __add__(self, other: 'Vector') -> 'Vector': # type: ignore[override]
        return Vector(self.x + other.x, self.y + other.y)
    
    """
    ## Your current code is fine:
    Your original implementation without `@overload` works perfectly for the single case of adding two vectors. 
    You only need `@overload` when you want to support multiple different parameter types with different return types.

    The `# type: ignore[override]` comment you have is handling the fact that `NamedTuple.__add__` returns `tuple`, 
    but you're changing it to return `Vector`.
    """


# fmt: on

v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1 + v2)  # Vector(x=4, y=6)
