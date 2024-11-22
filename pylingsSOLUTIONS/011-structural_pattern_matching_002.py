# using dataclass define class User and show that
# in structural pattern matching -> pattern is not your typical expression
# but subject is
# put it simple:
# subject is expresion -> is executed;
# pattern looks like it is executed but it is only notation for Class Pattern

from dataclasses import dataclass
from typing import ClassVar


@dataclass
class User:
    name: str
    couter: ClassVar[int] = 0

    def __post_init__(self):
        print(f"Created a new user name {self.name}")
        User.couter += 1


match User("Adam"):
    case User("Ewa"):
        pass


print(f"{User.couter=}")
assert User.couter == 1
assert User.couter != 2
