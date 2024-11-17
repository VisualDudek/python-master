# bare-bone Python REPL
# TAKEAWAY: cascade of nested `match` statements, optional guard, capture pattern

import sys
import traceback


PROMPT = "\N{snake}"
COMMANDS = ("help", "exit", "quit")


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
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")
        except EOFError:
            print()
            exit()
        except Exception:
            traceback.print_exc(file=sys.stdout)


if __name__ == "__main__":
    main()
