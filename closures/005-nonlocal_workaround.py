# With immutable - needs explicit nonlocal
def outer():
    count = 0
    def inner():
        nonlocal count  # Explicit: "I want to rebind outer's count"
        count += 1      # Assignment/rebinding
    return inner

# With mutable - implicit nonlocal behavior
def outer():
    count = [0]
    def inner():
        # No nonlocal needed!
        count[0] += 1   # Reading count from outer scope, modifying its contents
    return inner