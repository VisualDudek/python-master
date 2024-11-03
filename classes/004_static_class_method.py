# learn staticmethod vs. classmethod

# you "can create" classmethod using static method BUT it is cumbersome and breakes inheritance


class Calendar:
    @staticmethod
    def from_json(filename):
        c = Calendar()  # <----- seems clever but it is not
        ...
        return c


# vvvvvvvvvvvvvv POC how inheritance is break
class WorkCalendar(Calendar):
    pass


c = WorkCalendar.from_json(
    "my_calendar.cal"
)  # OUCH it will return Calendar BUT we expect WorkCalendar
