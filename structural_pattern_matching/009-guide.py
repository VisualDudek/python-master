# bare-bone Python REPL
# add executing given code
# TAKEAWAY: overlapping patterns

import ast
import sys
import traceback


PROMPT = "\N{snake}"
COMMANDS = ("help", "exit", "quit")


def valid(code: str):
    try:
        ast.parse(code)
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
                case statement if valid(statement):
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
