# change capture pattern + guard into Value Pattern with variable belong to some namespace
# use two diff namespaces

import enum


class ClassCommand:
    HELP = "help"


class EnumCommand(enum.StrEnum):
    EXIT = "exit"


match input("Type your command: "):
    case ClassCommand.HELP:
        print("Showing help")
    case EnumCommand.EXIT:
        exit()
    case _:
        print("Unknow command")
