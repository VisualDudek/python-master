import sys
from unittest.mock import patch


PROMPT = "\N{snake}"

# pyright: reportMatchNotExhaustive=false


# @patch("builtins.input", return_value="help")
def test_input():
    with patch("builtins.input", return_value="help"):
        match subject := input(PROMPT):
            case "help":
                print(f"{subject=}")
                return sys.version


assert test_input() == sys.version


@patch("builtins.input", return_value="help")
def test_input_decorator(mock_input):
    match subject := input(PROMPT):
        case "help":
            print(f"{subject=}")
            return sys.version


assert test_input_decorator() == sys.version
