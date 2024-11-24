# change capture pattern + guard into Value Pattern with variable belong to some namespace
# use two diff namespaces

HELP_COMMAND = "help"
EXIT_COMMAND = "exit"

match input("Type your command: "):
    case command if command == HELP_COMMAND:
        print("Showing help")
    case command if command == EXIT_COMMAND:
        exit()
    case _:
        print("Unknow command")
