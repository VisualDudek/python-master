# mock stdout

import unittest
from unittest.mock import patch
from io import StringIO


def f():
    print("Hello")


class TestF(unittest.TestCase):

    @patch("sys.stdout", new_callable=StringIO)
    def test_f(self, mock_stdout: StringIO):
        f()

        self.assertIn("Hello", mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
