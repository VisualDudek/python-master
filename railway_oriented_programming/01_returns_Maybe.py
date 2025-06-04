from dataclasses import dataclass

from returns.maybe import Maybe, Some, Nothing


@dataclass
class User:
    id: int
    name: str


USERS = {1: User(1, "Alice"), 2: User(2, "Bob")}

# Zobacz gdzie jest problem, chcech wyszukać User-a i zwrócić typ User
# ALE może się zdażyć że nie mam takiego id co powoduje że masz fn -> User | None
def find_user_legacy(user_id: int) -> User | None:
    return USERS.get(user_id, None)

# lub może przyjść Ci do głowy exception
def find_user_legacy(user_id: int) -> User:
    if user_id not in USERS:
        raise ValueError(f"User with id {user_id} not found")
    return USERS[user_id]


# Monadic approach:
def find_user(user_id: int) -> Maybe[User]:
    return Some(USERS[user_id]) if user_id in USERS else Nothing

# i teraz magia, Maybe ma zestaw uzytecznych metod z paradygmatu programowania funkcyjnego
result = find_user(1).map(lambda u: u.name)
print(result)

missing_result = find_user(3).map(lambda u: u.name) # KEY TAKEAWYA to nie gereruje błędu
# tylko zwraca <Nothing>
print(missing_result)