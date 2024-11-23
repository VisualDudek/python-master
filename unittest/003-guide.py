# you can use `patch` with `assert` for quick and simple patch, without `unittest.TestCase`

import enum

from unittest.mock import patch, Mock


class EnumCommand(enum.StrEnum):
    HELP = "help"
    EXIT = "exit"


def my_func():
    match input("Type your command: "):
        case EnumCommand.HELP:
            return "Showing help"
        case EnumCommand.EXIT:
            exit()
        case _:
            print("Unknow command")


def test_my_func():

    @patch("builtins.input", side_effect=["exit"])
    @patch("builtins.exit", side_effect=None)
    def test_with_mocked_exit(mock_exit: Mock, _):
        my_func()

        assert mock_exit.called is True
        assert mock_exit.call_count == 1

    test_with_mocked_exit()


if __name__ == "__main__":
    test_my_func()
