# metaclasses
# TAKEAWAY: all clases inherit from the `type` metaclass
# - the `type` metaclasses has a `__call__` method
# - the `__call__` invokes `__new__` and `__init__`
# - default methods for `__new__` and `__init__` are provided in the class hierarchy
# - `__new__` is resposible for obj. creation, PyDocs:
# Called to create a new instance of class cls. __new__() is a static method
# (special-cased so you need not declare it as such) that takes the class of
# which an instance was requested as its first argument.
# The remaining arguments are those passed to the object constructor expression
# (the call to the class). The return value of __new__() should be
# the new object instance (usually an instance of cls).


# vvvvvvv here you learn how now object is created
def new(cls):
    obj = object.__new__(cls)
    obj.desc = "Tha is a suprise"
    return obj


A = type(
    "A", (), {"__new__": new}
)  # if fact this is meta class bc it change how obj is created

a = A()
print(f"{a.desc=}")
