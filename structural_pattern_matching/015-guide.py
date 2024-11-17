# capture pattern + guard
# TAKEAWAY: leads to overly verbose code -> SOLUTION: value pattern

HELP_COMMAND = "help"
EXIT_COMMAND = "exit"

match input("Type your command: "):
    # VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
    case command if command == HELP_COMMAND:
        print("Showing help")
    case command if command == EXIT_COMMAND:
        exit()
    case _:
        print("Unknow command")
