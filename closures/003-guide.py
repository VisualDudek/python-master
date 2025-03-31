# Encapsulation and Data Hiding With Closures

# ale łądnie pokazany shadowing zmiennych na przykłądzie zmiennej password
# ^^^ jednak nie, nie zauważyłem różnicy pomiędzy `password` a `passwd`


def create_secure_data(data: str, password: str = "secret"):
    password = password  # hidden variable in outer function

    def get_data(passwd: str) -> str | None:
        if passwd == password:
            return data  # access allowed to outer data
        else:
            return None  # access denied

    return get_data


# Usage:
secure_data = create_secure_data("my sensitive data")
print(secure_data("secret"))  # Output: "my sensitive data"
print(secure_data("wrong password"))  # Output: None
