# using dataclass define class User and show that
# in structural pattern matching -> pattern is not your typical expression
# but subject is
# put it simple:
# subject is expresion -> is executed;
# pattern looks like it is executed but it is only notation for Class Pattern

from dataclasses import dataclass


class User: ...


assert User.couter == 1
assert User.couter != 1
