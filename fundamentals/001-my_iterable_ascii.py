# just practice Iterable Protocol

import string


class MyIterableASCII:
    def __init__(self, start: int = 0):
        self.data = string.ascii_uppercase
        self.index = start

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
my_iterable = MyIterableASCII(23)
values = [_ for _ in my_iterable]
assert values == ["X", "Y", "Z"]
