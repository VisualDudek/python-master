from typing import NamedTuple, Optional


class Point(NamedTuple):
    x: int
    y: int
    desc: Optional[str] = None


p = Point(11, 22)

x, y, _ = p
sum = p.x + p.y

print(p)
