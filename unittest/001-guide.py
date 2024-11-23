# my example how to test structural patteran matching while patching builtins input() function
# ??? how to test exit() ?

import enum
import unittest

from unittest.mock import patch


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

    def test_my_func(self):
        expected_output = "Showing help"

        with patch("builtins.input", side_effect=["help"]):

            self.assertEqual(my_func(), expected_output)


if __name__ == "__main__":
    unittest.main()
