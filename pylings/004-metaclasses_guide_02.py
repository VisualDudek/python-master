# use type() and create class C same as B


class A:
    pass


class B(A):
    description = "Things inside things"

    def __str__(self):
        return f"This is my custom dunder __str__ = {self.description}"


b = B()
print(f"{type(b)=}")
print(f"{isinstance(b, A)=}")
print(f"{b.description=}")
print(f"{str(b)=}")

# TODO: implement calss C using type()
C = type("C", (), {})


# Tests
c = C()
assert isinstance(c, A) == True
assert c.description == "Things inside things"
assert str(c) == "This is my custom dunder __str__ = Things inside things"
