# how to test builtins.exit, how to test that exit was called?

import enum
import unittest

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


# VVVVVVVVVVVVVVVVVVV
class TestMyFunc(unittest.TestCase):

    @patch("builtins.input", side_effect=["exit"])
    @patch("builtins.exit")
    # ---------------------------vvvvvvv type annotate
    def test_exit(self, mock_exit: Mock, _):
        my_func()

        # mock_exit.assert_called_once()
        self.assertTrue(mock_exit.called)
        self.assertEqual(mock_exit.call_count, 1)


if __name__ == "__main__":
    unittest.main()
