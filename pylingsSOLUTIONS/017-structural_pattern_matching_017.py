# What is wrong with this code?
# Fix it
from unittest.mock import patch
import enum


# vvvvvvvvvvvvvvvvvvvvvvvvvvvvv
class EnumCommand(enum.StrEnum):
    HELP = "help"


# class CMD:
#     HELP = "help"


# ruff: noqa
def foo():
    with patch("builtins.input", side_effect=["exit"]):
        match input("Type your command: "):
            case EnumCommand.HELP:
                print("Showing help.")
            case "exit":  # type: ignore
                return "exit"
            case _:
                pass


assert foo() == "exit"
