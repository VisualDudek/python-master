# decorator as a class

# TAKEAWAY: diff between '__call__' and '__get__'
# Purpose: __call__ allows an instance of a class to be called like a function.
# Usage: If an object defines a __call__ method, it can be invoked with () parentheses,
# just like a regular function.
# Purpose: __get__ is part of Python’s descriptor protocol and customizes attribute access.
# Usage: __get__ is used when an object is an attribute of another class
# and is meant to control how that attribute is accessed.
# It is most commonly used in property decorators or descriptors.
# TAKEAWAY: object.__call__(self[, args...]) vs. object.__get__(self, instance, owner=None)


class AccessLogger:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self  # when the attrib is accessed through the owner
        print(f"Accessing '{self.func.__name__}' method of {owner.__name__} class.")
        return self.func.__get__(instance, owner)  # Delegate to the original function


class Loggable:
    # vvvvvvvvvvvvvvvvvvvv
    # wrap greet fn. with an instance of AccessLogger,
    # when obj.greet is accessed, it triggers AccessLogger.__get__
    @AccessLogger
    def greet(self):
        return "Hello!"

    # vvvvvvvvvvvvvvvvvvvvv
    # Instead of using @AccessLogger, directly create an instance of AccessLogger
    greet = AccessLogger(lambda self: "Hello!")


# Usage
obj = Loggable()
print(obj.greet())  # Logs access and calls the method
