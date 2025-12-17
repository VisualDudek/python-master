"""
Why NamedTuple here is not a good idea? -> NamedTuple instances are immutable
How to fix it? -> use dataclass 
"""

# from typing import NamedTuple
from dataclasses import dataclass

@dataclass # you can do even better with @dataclass(slots=True)
class Point:
    x: int
    y: int

p = Point(0, 0)

for i in range(5):
    p.x += 1  
    print(p)