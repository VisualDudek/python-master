# Encapsulation and Data Hiding With Closures


# zaimplementuj fn. zabezpieczoną hasłem


def create_secure_data(data: str, password: str = "secret"):
    # WRITE YOUR CODE HERE
    pass


# --- TESTING ---


secure_data = create_secure_data("my sensitive data")
assert secure_data("secret") == "my sensitive data"
assert secure_data("wrong password") is None
