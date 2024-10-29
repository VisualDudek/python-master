# __init__ vs. __new__
# how those two are called during object construction
# TAKEAWAY: __new__ returns obj. __init__ do not return anything
# - __new__ take class and return its instance
# - __init__ takes ^^^^^^^^^^^^^^^^^^^^^^^^^^^ instance and set/init default values


class A:
    def __new__(cls, *args, **kwargs):
        print("called new", cls, args, kwargs)
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print("called init", self, args, kwargs)


# how object construction works
a = A(1, 2, 3, x=4)
