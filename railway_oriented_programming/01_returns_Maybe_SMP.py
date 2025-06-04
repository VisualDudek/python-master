from dataclasses import dataclass

from returns.maybe import Maybe, Some, Nothing


@dataclass
class User:
    id: int
    name: str


USERS = {1: User(1, "Alice"), 2: User(2, "Bob")}


def find_user(user_id: int) -> Maybe[User]:
    return Some(USERS[user_id]) if user_id in USERS else Nothing


def handle_user_data(user_id):
    match find_user(user_id):
        case Some(user):
            print(f"User found: {user.name}")
        case Nothing:
            print("No user found")


def main() -> None:
    handle_user_data(1)
    handle_user_data(3)


if __name__ == "__main__":
    main()