# define fn: structural_pattern_matching
# Learning Curve: `AliasTypes` cannot be directly used as class patterns

from typing import TypeAlias, List

Number: TypeAlias = int | float


# pyright: reportMatchNotExhaustive=false
def structural_pattern_matching(subject: List[Number]):
    match subject:
        case list([int() | float() as x, int() | float() as y, 0]):
            return f"Point({x=}, {y=})"


assert structural_pattern_matching([1, 2, 0]) == "Point(x=1, y=2)"
