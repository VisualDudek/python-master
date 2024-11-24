# you can parse iterable using **Sequence Pattern**


import enum
import shlex


class EnumCommand(enum.StrEnum):
    GIT_COMMIT = "git commit -a -m 'Initial commit'"
    GIT = "git"
    GIT_VERSION = "git version"
    EMPTY = ""


print(shlex.split(EnumCommand.GIT_COMMIT))


match shlex.split(EnumCommand.GIT_COMMIT):
    case []:
        print("Empyt sequence")
    case ["git"]:
        print("Showing the list of available Git subcommands.")
    case ["git", "--version"]:
        print("Showing the version of your Git clinet.")
    case ["git", subcommand, *options]:
        print(f"{subcommand=}, {options=}")
    case _:
        pass
