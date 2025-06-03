from typing import TypedDict

class User(TypedDict):
    """
    A TypedDict for user information.
    
    Attributes:
        name (str): The name of the user.
        age (int): The age of the user.
    """
    name: str
    age: int

def main() -> None:
    users: list[User] = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 17},
    ]

    adult_users: list[User] = []

    # Imperative approach to filter adult users
    for user in users:
        if user['age'] >= 18:
            adult_users.append(user["name"].upper())

    