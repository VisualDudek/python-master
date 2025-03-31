"""
In Python, closures are a programming concept where a nested
function remembers the values from its enclosing scope,
even if that scope has finished executing.
"""


# Example
def outer(x: int):
    def inner(y: int):
        return x + y
        #     ^^^ uses x from outer's scope

    return inner


add5 = outer(5)
print(add5(3))  # Outputs: 8
