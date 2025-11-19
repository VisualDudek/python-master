"""
__closure__ is a dunder (double underscore) attribute that contains
the closure data for a function.

What it stores:

A tuple of cell objects
Each cell holds a variable captured from the enclosing scope
None if the function is not a closure
"""
def make_stats_tracker():
    stats = {"count": 0}  # This gets captured
    
    def add_value(value):
        stats["count"] += 1
    
    return add_value

tracker = make_stats_tracker()

# Inspect the closure
print(tracker.__closure__)  
# (<cell at 0x...: dict object at 0x...>,)

# Access the captured variable
print(tracker.__closure__[0].cell_contents)
# {'count': 0}

# Multiple captured variables
def multi_closure():
    x = 1
    y = 2
    def inner():
        return x + y
    return inner

fn = multi_closure()
print(fn.__closure__)  # (<cell...>, <cell...>) - two cells
print(fn.__closure__[0].cell_contents)  # 1 (x)
print(fn.__closure__[1].cell_contents)  # 2 (y)