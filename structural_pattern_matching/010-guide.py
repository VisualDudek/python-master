# bare-bone Python REPL
# add `eval`
# TAKEAWAY: expressions are statements, but not the other way around, Literal

import ast
import sys
import traceback
from typing import Literal


PROMPT = "\N{snake}"
COMMANDS = ("help", "exit", "quit")


def valid(code: str, mode: Literal["eval", "exec"]):
    try:
        ast.parse(code, mode=mode)
        return True
    except SyntaxError:
        return False


def main():
    while True:
        print('Type "help" for more inforamtion, "exit" or "quit" to finish.')
        try:
            match subject := input(PROMPT):
                case (
                    command
                ) if command.lower() in COMMANDS:  # this is tricky, having warlus above
                    match command.lower():
                        case "help":
                            print(f"Python {sys.version}")
                        case "exit" | "quit":
                            break
                case expression if valid(expression, "eval"):
                    _ = eval(expression)
                    if _ is not None:
                        print(_)
                case statement if valid(statement, "exec"):
                    exec(statement)
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")
        except EOFError:
            print()
            exit()
        except Exception:
            traceback.print_exc(file=sys.stdout)


if __name__ == "__main__":
    main()
