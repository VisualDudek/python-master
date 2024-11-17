# structural pattern is the opposite of object construction.
# It's the "left side" of the assignment statement,
# conceptually similar to tuple unpacking
# BUT unpacking can fail, whereas pattern mattching is conditional, so it'll only run
# if the pattern matches the subject.

# vvvvvv <----------------------------------
a, b, c = range(3)  #                       \
print(f"Pint({a=}, {b=}, {c=})")  #         |
#                                           |
#                                           |
match range(3):  #                          |
    # vvvvvvvvvvv                           |
    case x, y, z:  # -------- the same as --/
        print(f"Pint({x=}, {b=}, {z=})")


# unpacking can fail
try:
    a, b, c = range(2)
except ValueError as e:
    print(e)


# pattern matting is conditional
match range(2):
    case x, y, z:
        # vvvvvvvv will not run, will not raise exception
        print(f"Pint({x=}, {b=}, {z=})")
