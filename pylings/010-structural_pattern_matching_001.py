# define fn: structural_pattern_matching

from typing import TypeAlias, List

Number: TypeAlias = int | float


# pyright: reportMatchNotExhaustive=false
def structural_pattern_matching(subject: List[Number]):
    pass


assert structural_pattern_matching([1, 2, 0]) == "Point(x=1, y=2)"
