import itertools

# _N = TypeVar(
#    "_N", int, float, SupportsFloat, SupportsInt, SupportsIndex, SupportsComplex
# )

# iterator that returns evenly spaced values beginning with start.
# by default repeates indefinitely
counter: itertools.count = itertools.count(start=0, step=1)
values = [next(counter) for _ in range(5)]
assert values == [0, 1, 2, 3, 4]

counter: itertools.count = itertools.count(start=10, step=2)  # type: ignore
values = []
for _ in range(5):
    values.append(next(counter))
assert values == [10, 12, 14, 16, 18]


# roughly equivalent to generator below
def count(start: int = 0, step: int = 1):
    n = start
    while True:
        yield n
        n += step


# which using itertools.count looks like this
for _ in itertools.count(start=0, step=1):
    ...
