# ensure strict type checking using class pattern


def is_adult(age):
    match age:
        case int(18):
            return True
        case _:
            return False


is_adult(18)  # True
is_adult(18.0)  # False
is_adult(18.0 + 0.0j)  # False
