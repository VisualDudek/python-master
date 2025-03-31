"""
In Python, closures are a programming concept where a nested
function remembers the values from its enclosing scope,
even if that scope has finished executing.
"""

# napisz fn. factory: powerToX


def outer(x: int):
    # WRITE YOUR CODE HERE
    pass


# --- TESTING

powerTo2 = outer(2)
assert powerTo2(5) == 25
assert powerTo2(2) == 4

powerTo3 = outer(3)
assert powerTo3(2) == 8
