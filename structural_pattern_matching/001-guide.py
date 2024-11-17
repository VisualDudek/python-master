# compare following thow block of code with same functionality
# SPM is more readable and have declarative style


def structural_pattern_matching(subject):
    match subject:
        case list([int() | float() as x, int() | float() as y, 0]):
            print(f"Point({x=}, {y=})")


def legacy_code(subject):
    if isinstance(subject, list) and len(subject) == 3:
        if (
            isinstance(subject[0], int | float)
            and isinstance(subject[1], int | float)
            and subject[2] == 0
        ):
            x, y, _ = subject
            print(f"Point({x=}, {y=})")


structural_pattern_matching([1, 2, 0])
legacy_code([1, 2, 0])
