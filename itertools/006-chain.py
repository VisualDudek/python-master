from itertools import chain

# chain(*iterables) -> iterator
values = list(chain([1, 2, 3], [4, 5], [6]))
assert values == [1, 2, 3, 4, 5, 6]

# nice usecase: combining diff types of Iterables
list1 = [1, 2, 3]
tuple1 = (4, 5)
set1 = {6, 7}
values = list(chain(list1, tuple1, set1))
assert values == [1, 2, 3, 4, 5, 6, 7]
