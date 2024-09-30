from itertools import compress, cycle
from typing import List, Iterator

# Takeaway: similar to filter(predicate, iterable)
# Key Takeaway: cycle(List[bool]) -> Iterator[bool]
# compress(iterable, selectors) -> iterator
data: List[int] = [1, 2, 3, 4, 5]
selectors = [True, False, True, False, True]
values = list(compress(data=data, selectors=selectors))
assert values == [1, 3, 5]


# Usecases: combine with cycle
data: List[str] = ["A", "B", "C", "D", "E"]
selectors: Iterator[bool] = cycle([True, False])  # clever way to create selector
values = list(compress(data=data, selectors=selectors))
assert values == ["A", "C", "E"]
