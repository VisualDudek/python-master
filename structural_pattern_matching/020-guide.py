# use start operator to match sequence of lenght two or more.

match range(2):
    case [first, second, *_]:
        print("This will match seq. of lenght two or more.")
    case _:
        pass

# vvvvvvvvvvvvvvvvvvvv compare to without star operator
match (1, 2, 3):
    case [x, y]:  # type: ignore
        print(f"{x=}, {y=}")
    case _:
        print("Will only match two-tuple")
