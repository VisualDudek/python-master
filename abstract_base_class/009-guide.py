# TAKEAWAY: Use protocol definitions as types ALSO in type hints
# SEE do_read and do_write fn.
# TAKEAWAY: Employning protocols as types in fn. U can have cass definitions
# that do not have any relations with Writable or Readable protocol SEE Author

from typing import Protocol
import abc


class Writable(Protocol):
    def write(self, data: dict) -> None:
        """This method should write dictionary data."""


class Readable(Protocol):
    @abc.abstractmethod
    def read(self) -> dict:
        """This method should return a dictionary."""


# SEE THIS:
def do_read(reader: Readable) -> dict:
    return reader.read()


# SEE THIS:
def do_write(writer: Writable, data: dict) -> None:
    writer.write(data)


class Author:
    def __init__(self, name: str):
        self.name = name

    def write(self, data: dict) -> None:
        print(f"{self.name} is writing {data}")


def main():
    data = {"name": "John Doe", "age": 30}
    author = Author("John")
    do_write(author, data)


if __name__ == "__main__":
    main()
