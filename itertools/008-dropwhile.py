from itertools import dropwhile
from typing import List, Iterator

# dropwhile(predicate, iterable) -> Iterator
data: List[int] = [1, 2, 3, 4, 5, 1, 2, 3]
values: List[int] = list(dropwhile(lambda x: x < 3, data))
assert values == [3, 4, 5, 1, 2, 3]
# TAKE NOTE that only initial values less than 3 was droped

# Usecase: Process Log Files after a certain timestamp
