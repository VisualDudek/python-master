# bare-bone Python REPL
# add main loop
# TAKEAWAY: traceback module, subpattern union

import sys
import traceback


PROMPT = "\N{snake}"


def main():
    while True:
        print('Type "help" for more inforamtion, "exit" or "quit" to finish.')
        try:
            match subject := input(PROMPT):
                case "help":
                    print(f"Python {sys.version}")
                case "exit" | "quit":
                    break
        except Exception:
            traceback.print_exc(file=sys.stdout)


if __name__ == "__main__":
    main()
