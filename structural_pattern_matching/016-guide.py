# **Value Pattern** let you recognize variables that should be treated as constans,
# typically belong to some namespace, such as a class, enum or a Ptyhon module,
# which you can access with the dot operator.

import enum


class ClassCommand:
    HELP = "help"


class EnumCommand(enum.StrEnum):
    EXIT = "exit"


match input("Type your command: "):
    case ClassCommand.HELP:
        print("Showing help.")
    case EnumCommand.EXIT:
        exit()
