# Another example how duck typing collide with type hints
# and why quick fix can be cumbersome.
# next: what if you want define your own protocol


def mean(grades: list) -> float:
    return sum(grades) / len(grades)


# ^^^^^ in fact fn: mean will work on anything that suports `.__iter__()` and `len()`

assert mean([4, 3, 3, 4, 5]) == 3.8  # works with list
assert mean((4, 3, 3, 4, 5)) == 3.8  # works with set


# quick fix
def mean_union(grades: list | tuple | set) -> float:
    return sum(grades) / len(grades)


# works but idealy you wand type hist that is generic for `.__iter__()` and `len()`
assert mean_union([4, 3, 3, 4, 5]) == 3.8
assert mean_union((4, 3, 3, 4, 5)) == 3.8

# SOLUTION
# use already defined interface based on abc
from collections.abc import Collection


def mean_collection(grades: Collection) -> float:
    return sum(grades) / len(grades)


assert mean_collection([4, 3, 3, 4, 5]) == 3.8
assert mean_collection((4, 3, 3, 4, 5)) == 3.8
