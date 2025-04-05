"""
Currying is a functional programming concept where a function with multiple
arguments is transformed into a sequence of functions, each taking
one argument at time.
"""


def add(x: int, y: int):
    return x + y


# transform add fn. into a series of function,each taking one arg.
def curried_add(x: int):
    def inner(y: int):
        return x + y

    return inner


add_5 = curried_add(5)
print(add_5(3))  # Output: 8
