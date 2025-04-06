from collections import namedtuple

# wstęp do NamedTuple

# Basic example
Point = namedtuple("Point", ["x", "y"])  # type: ignore
# field_names ["x", "y"] alternatively can be single string:
# `x y` or `x, y`

p = Point(11, y=22)  # instantiate with pos. or keyword args
# p[0] + p[1]   indexable like the plain tuple

x, y = p  # unpack linke a regular tuple

# NAJWIĘKSZA WARTOŚĆ DODANA
sum = p.x + p.y  # type: ignore
# fields also accessible by name

print(p)  # readable __repr__ with a name=value style
