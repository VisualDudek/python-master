from collections import namedtuple


#                     vvvvv is the name of the type
MyPoint = namedtuple("Point", ["x", "y"])  # type: ignore
# ^^^^^^^ just the variable name

p = MyPoint(1, 2)

print(p)  # Prints: Point(x=1, y=2)
