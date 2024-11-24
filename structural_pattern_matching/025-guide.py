# instead of explicit calling `isinstance()` on the subject,
# you can check if the subject is an instance of the given
# type by using a class pattern.

# Great example how to parse time, it alows to drop all supid fn. such
# as timefromstring, timefromint, timefromstamp


from datetime import UTC, datetime
from typing import Any, TypeAlias

Time: TypeAlias = int | float | str | datetime


def parse(value: Any):
    match value:
        case datetime():
            return value.astimezone(UTC)
        case int() | float():
            return datetime.fromtimestamp(value, UTC)
        case str():
            return datetime.fromisoformat(value).astimezone(UTC)
        case _:
            raise TypeError(f"Unsapported type: {type(value)}")


dates: list[float | str] = [
    -14182967.876544,
    "1969-07-20T20:17:12.123456+00:00",
]
# OR you can use TypeAlias -> dates: list[Time]

for date in dates:
    print(parse(date))

# below you will find interensting failures

# date: Union[str, float]
# for date in ["1969-07-20T20:17:12.123456+00:00", float(-14182967.876544)]:
#     print(parse(date))

# for _ in ["1969-07-20T20:17:12.123456+00:00", -14182967.876544]:
#     print(parse(_))
