"""
- implement math.dist using sum generator expression and zip
"""

from math import sqrt, dist

def zip_dist(a: tuple[float, ...], b: tuple[float, ...]) -> float:
    """Calculate the Euclidean distance between two points using zip and a generator expression."""
    pass

p0 = (0.0, 0.0, 0.0)
p1 = (1.0, 2.0, 3.0)

assert zip_dist(p0, p1) == dist(p0, p1)