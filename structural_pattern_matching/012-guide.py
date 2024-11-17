# you can reuse the underscore several times as a subpattern
# to discard certain elements of other patterns.

from dataclasses import dataclass


@dataclass
class User:
    name: str
    family: str
    age: int


match user := User("Marcin", "D", 42):
    case User(_, _, age) if age < 18:
        print(f"Underage: {user}")
    case User(_, "D", _):
        print(f"D family member: {user}")
