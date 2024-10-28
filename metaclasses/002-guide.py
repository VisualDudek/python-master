# How to take advantego of type() ?
# Create class without class key word


class A:
    pass


print(f"{type(A())=}")
print(f"{type(A)=}")

# vvvvvvvvvvvvvvvvvvv
B = type("B", (), {})

print(f"{type(B())=}")
print(f"{type(B)=}")


# vvvvvv now something more coplicated, inherit and define class attribute
BB = type(
    "BB",
    (B,),
    {"description": "This is a class attribute shared by all obj. instances"},
)

print(f"{type(BB())=}")
print(f"{type(BB)=}")
bb = BB()
print(f"{isinstance(bb, B)=}")
print(f"{bb.description=}")


# vvvvv now add simple class method
C = type(
    "C",
    (B,),
    {
        "description": "Things inside things",
        "content_count": 1,
        "total_things": lambda x: x.content_count + 1,
    },
)

c = C()
print(f"{type(c)=}")
print(f"{isinstance(c, B)=}")
print(f"{c.content_count=}")
print(f"{c.total_things()=}")
print(f"{str(c)=}")


# vvvvvv lambda limits Us to simple onliners, create "full" class method
# override dunder '__str__' method
def to_string(obj):
    return f"This is my string representation= {obj.description}"


D = type(
    "D",
    (B,),
    {"description": "Things inside things", "__str__": to_string},
)

d = D()
print(f"{str(d)=}")  # now str() is calling my dunder "__str__" -> `to_string`
