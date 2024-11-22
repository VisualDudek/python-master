# bare-bone Python REPL

import sys


PROMPT = "\N{snake}"

# pyright: reportMatchNotExhaustive=false

# match input(PROMPT):
# vvvvvvvv better bind subject to variable using warlus operator
match subject := input(PROMPT):
    case "help":
        print(f"Python {sys.version}")
