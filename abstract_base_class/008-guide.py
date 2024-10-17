# TAKEAWAY: Class can inherit from several protocols, SEE ReadWriteable class
# TAKEAWAY: Use protocol definitions as types ALSO in type hints SEE next file
# protocol duck-typing pitfall: wirite and read is not implemented and no one complains about it
#           ^^^^^^^^^^^^^^^^^^ SOLUTION: can use abstractmethod same as for ABC, SEE read method
#                                                                         in Readable Interface
# TAKEAWAY: protocols can also use abc.abstractmethod

from typing import Protocol
import abc


class Writable(Protocol):
    def write(self, data: dict) -> None:
        """This method should write dictionary data."""


class Readable(Protocol):
    @abc.abstractmethod
    def read(self) -> dict:
        """This method should return a dictionary."""


class ReadWritable(Readable, Writable):
    def __str__(self):
        return f"{self.__class__.__name__}()"


def main():
    data = {"name": "John Doe", "age": 30}
    handlers = ReadWritable()
    handlers.write(data)
    print(handlers.read())


if __name__ == "__main__":
    main()
