# using warlus operator store `match statement` subject in variable
# use input() as example and litteral pattern, if "help" then print python version
# mock build-in `input()`

import sys

PROMPT = "\N{snake}"

# pyright: reportMatchNotExhaustive=false


def test_input():
    pass


assert test_input() == sys.version
