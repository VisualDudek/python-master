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

    # Declarative approach to filter adult users
    adult_names = filter(lambda user: user['age'] >= 18, users)
    adult_users = [user['name'].upper() for user in adult_names]

    print(adult_users)

if __name__ == "__main__":
    main()

# Lines 22-23
# zwróć uwagę że nie potrzebujesz typowania,
# ponieważ filtrujesz poprzez listę TypedDict