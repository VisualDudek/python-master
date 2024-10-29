# fix from prev. file
# how __new__ help when __init__ cannot
# TAKEAWAY: writing own class that proxy built in type is stupid idea due to performance reasons


class UppercaseTuple(tuple):

    def __new__(cls, iterable):
        print(f"called new with: {iterable=}")
        upper_iterable = (s.upper() for s in iterable)
        return super().__new__(cls, upper_iterable)


print(f"{UppercaseTuple(["hi", "there"])=}")
