# __new__ was added into Python, primarly to allow
# programmers to subclass built-in immutable
# if you want subclass tuple to create UppercaseTuple you can be tempted to do this
# using __init__ but it is to late, see below:
# see fix in next file


class UppercaseTuple(tuple):

    def __init__(self, iterable):
        print(f"called init with: {iterable=}")
        for i, arg in enumerate(iterable):
            self[i] = arg.upper()


print(f"{UppercaseTuple(["hi", "there"])=}")
