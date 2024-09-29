from itertools import batched, islice

# Key takeaway: input is consumed lazily, just enough to fill a batch.
# The result is yielded as soon as the batch is full or
# when the input iterable is exhausted
# batched(iterable, n:int)
values = list(batched("ABCDE", 2))
assert values != [("A", "B"), ("C", "D"), ("E")]
assert values == [("A", "B"), ("C", "D"), ("E",)]
# This is interesting ("E") != ("E",)


# Roughly equivalent to:
def _batched(iterable, n):
    # batched('ABCDEFG', 3) → ABC DEF G
    if n < 1:
        raise ValueError("n must be at least one")
    iterator = iter(iterable)
    while batch := tuple(islice(iterator, n)):  # nice usage of warlus operator
        yield batch


# Advanced Exercises

## Batching with Conditional Breaks:
# ? can you eliminate usage of list and as above just use iterators?
from typing import Iterable, Callable, Any


def conditional_batches(iterable: Iterable, condition: Callable[[Any], bool]):
    batch: list[Any] = []
    for item in iterable:
        if condition(item):
            yield tuple(batch)
            batch = []
        batch.append(item)
    # final batch
    if batch:
        yield tuple(batch)


values = list(conditional_batches([1, 2, 0, 4, 5], lambda x: x == 0))
assert values == [(1, 2), (0, 4, 5)]

# TODO
## Batching with Dynamic Sizes

# TODO
## Batching with Padding: pad last batch witch a specified value if is not full.
