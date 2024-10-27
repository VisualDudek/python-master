# holy grail of understanding:
# 1. you know that `__new__` is called when you create new obj.
# 2. you want to do something when a class(object) is created
# 3. you have a briliant idea that you will override `type.__new__` OUCH !!!
# 4. you learn that you cannot override `type.__new__`
# 5. you learn that SOLUTION to above is:
#   - create a special class that inherits from `type`
#   - override `__new__` on that class
#   - use the special metaclass ^^^^^^ when declaring another class via key word "metaclass"
# see example: create MetaClass that count how many classes were created, NOT instances
# TAKEAWAY: you can hook when a programmer defines a class and do things with it, see next file
# for real world metaclasses


class CounterMeta(type):
    count = 0

    def __new__(cls, name, base, dct):
        kls = super().__new__(cls, name, base, dct)
        cls.count += 1  # THIS is mind bending
        return kls


# NOTE that this is only reference, there is no invokation
class A(metaclass=CounterMeta):
    pass


a = A()
aa = A()

try:
    print(a.count)
except AttributeError:
    print(
        """
          callind to 'a.count' gives AttributeError exception
          .count attrib is on MetaClass only, not on the class.
          you can get .count using __class__ dunder
          """
    )

print(f"{a.__class__.count=}")
assert (
    a.__class__.count == 1
)  # do not care about A instances, only about number of classes that use
# metaclass CounterMeta


class B(metaclass=CounterMeta):
    pass


b = B()
print(f"{b.__class__.count=}")
print(f"{a.__class__.count=}")
print(f"{aa.__class__.count=}")
