# What is wrong with this code?
# Fix it


from unittest.mock import patch

command = "help"


# ruff: noqa
def foo():
    with patch("builtins.input", side_effect=["exit"]):
        match input("Type your command: "):
            case command:  # type: ignore
                print("Showing help.")
            case "exit":  # type: ignore
                return "exit"


assert foo() == "exit"
