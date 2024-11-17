# pattern is not your typical expression

from dataclasses import dataclass


@dataclass
class User:
    name: str

    def __post_init__(self):
        print(f"Created a new user name {self.name}")


# VVVVVVVVVVVVV
match User("Alice"):  # create a new User instance
    case User("Bob"):  # do not create instance of User
        pass
