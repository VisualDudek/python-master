# Everything in Python is an object
# what is the top hierarchy obj. ?
# TAKEAWAY: Python do not idstinct beetwen string and char, both are type 'str'

print(f"{type(1)=}")

print(f"{type([1 ,2])=}")


s = "Marcin"
print(f"{type(s)=}")
print(f"{type(s[0])=}")


print(f"{type(max)=}")
print(f"{type(int)=}")


class Dog:
    pass


dog = Dog()

print(f"{type(dog)=}")
print(f"{type(Dog)=}")


print(f"{type(type)=}")
