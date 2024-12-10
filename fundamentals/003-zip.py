# playing with unpacking iterables with zip

from random import randint

n = 10

d = {(randint(0, n), randint(0, n)): randint(0, n * n) for _ in range(n)}

print(f"{d.keys()=}")

#          vvvvvvvv without unpacking it is single object
print(*zip(d.keys()))
print(*zip(*d.keys()))


print(f"{list(map(max, zip(*d.keys())))=}")
#                     ^^^^ why not just use unpacking here ???

iter = zip(*d.keys())

print(next(iter))
print(next(iter))


print(f"{list(map(max, *zip(*d.keys())))=}")
#                     ^^^ this unpack into two tuples
# Jakim cudem to działa ???

t1 = (4, 1)
t2 = (1, 4)
t3 = (5, 3)

print(f"{list(map(max, zip(t1, t2, t3)))=}")

print(f"{list(map(max, *zip(t1, t2, t3)))=}")
#                     ^^^ this i crazy, do not do this !!!
