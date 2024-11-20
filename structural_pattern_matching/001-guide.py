# compare following thow block of code with same functionality
# SPM is more readable and have declarative style
# TAKEAWAY: TypeAlias

from typing import TypeAlias, List

Number: TypeAlias = int | float


# pyright: reportMatchNotExhaustive=false
def structural_pattern_matching(subject: List[Number]):
    match subject:
        case list([int() | float() as x, int() | float() as y, 0]):
            print(f"Point({x=}, {y=})")


def legacy_code(subject):  # type: ignore
    if isinstance(subject, list) and len(subject) == 3:  # type: ignore
        if (
            isinstance(subject[0], int | float)
            and isinstance(subject[1], int | float)
            and subject[2] == 0
        ):
            x, y, _ = subject  # type: ignore
            print(f"Point({x=}, {y=})")


structural_pattern_matching([1, 2, 0])
legacy_code([1, 2, 0])
