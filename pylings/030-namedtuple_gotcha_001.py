"""
Why NamedTuple here is not a good idea?
How to fix it?
"""

from typing import NamedTuple

class Point(NamedTuple):
    x: int
    y: int

p = Point(0, 0)

for i in range(5):
    p.x += 1  