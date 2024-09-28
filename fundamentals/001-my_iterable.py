# To make class iterabel in Python, you need to implement the iterable protocol.
# This protocol involves defining two methods:
# 1. __iter__(self): return iterator object. The object can be the class itself
# (in which case the class is both an iterable and an iterator) or separate iterator class.
# 2. __next__(sefl): this method should return next item from the seq when called
# and raise StopIteration when there are no more items
# Q: How to check if an object is iterable?


class MyIterable:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self  # The class itself is the iterator

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


# Usage
my_iterable = MyIterable([1, 2, 3])
values = [_ for _ in my_iterable]
assert values == [1, 2, 3]

# Check if my_iterable is Iterable using collections.abc:
from collections.abc import Iterable

assert isinstance(my_iterable, Iterable)
