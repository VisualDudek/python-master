import itertools


# iterator that returns object over and over again.
# Runs indefinitely unless the times argument is specified.

# itertools.repeate(object[, times])
repeater = itertools.repeat(10, 3)
values = list(repeater)
assert values == [10, 10, 10]


# Roughly equivalent to:
def repeat(object, times=None):
    if times is None:
        while True:
            yield object
    else:
        for i in range(times):
            yield object


# A common use is to supply a stream of constant values to map or zip:
# example with map:
values = list(map(pow, range(5), itertools.repeat(2)))
assert values == [0, 1, 4, 9, 16]
# bc map(function, iterable, *iterables)
# below example will fail at runtime:
# map(pow, range(2), 2)


# example with zip:
# zip(*iterables, strict=False)
values = list(zip(itertools.repeat(1), ["a", "b", "c"]))  # type: ignore
assert values == [
    (1, "a"),
    (1, "b"),
    (1, "c"),
]
