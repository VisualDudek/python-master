# Python Enum class uses the metaclass EnumType
# TAKEAWAY: dunder __prepare__() hook
# - this is a hook for the dict passed into __new__
# - can be used to add or modify the dict
# - EnumType is using it to convert its args to the EnumDict class


class Fruit(Enum):
    APPLE = 1
    PEAR = 2


# ^^^^^^ is-a vvvvvvv
class Enum(metaclass=EnumType): ...

# ^^^^^^ is-a vvvvvvv

class EnumType(type):
    __prepare__(...):
        # Prepare calling dict
        # with APPLE and PEAR
        ...
    # ^^^^^^ has-a -> class EnumDict(dict): ...
    
    __new__(...):
        # Construct class
        ...