from itertools import accumulate

# as defalut think as running total sum with first element unchanged
# Key takeaway:
# accumulate result from provided binary function
# accumulate(iterable[, func=operator.add, *, initial=None])
values = list(accumulate([1, 2, 3, 4, 5]))
assert values == [1, 3, 6, 10, 15]

# use cases:
# 1. running munimum
values = list(accumulate([1, 2, 3, 4, 5], min))
assert values == [1, 1, 1, 1, 1]

# see `functools.reduce()` for a similar fn. that returns
# only the final accumulated value

# 2. cumulative difference
# it is not diff between each two elements BUT accumulated diff
import operator

values = list(accumulate([10, 1, 2, 3, 4], operator.sub))
assert values == [10, 9, 7, 4, 0]
assert values != [10, 9, 1, 1, 1]

# 3. cumulative concat
values = list(accumulate(["a", "b", "c"], str.__add__))  # type: ignore
assert values == ["a", "ab", "abc"]
