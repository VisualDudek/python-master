# you can use kwargs of the class constructor to extract attribute values, positional args are not supported out of the box, class pattern needs to specify attributes order using `.__match_args__`

import datetime
from typing import NamedTuple


def aoc_status(date: datetime.date):
    match date:
        case datetime.date(year=_, month=12, day=1):
            print("Advent of Code starts today!")
        case datetime.date(year=_, month=12, day=day) if day <= 25:
            print(f"{25-day} days until the end of AoC.")
        case _:
            print("Sorry, no Advent of Code today.")


aoc_status(datetime.date.today())
aoc_status(datetime.date(2024, 12, 1))
aoc_status(datetime.date(2024, 12, 2))


class Date(NamedTuple):
    year: int
    month: int
    day: int


print(Date.__match_args__)

match Date(1969, 7, 20):
    case Date(_, 7, 20):
        print("Celebrating another moon landing anniversary!")
    case _:
        pass

try:
    datetime.date.today().__match_args__  # type: ignore
except AttributeError:
    print("'datetime.date' object has no attribute '__match_args__'")
