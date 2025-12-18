"""
SOLUTION
Show me usage of map with infinite built-in iterator.
I want to see that map is lazy and saves memory.
"""

from itertools import count, islice


points = map(lambda x: (x, x**2), count())

for i in islice(points, 5):
    print(i)
