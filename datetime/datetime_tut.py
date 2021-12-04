# timedelta: represents duration, the difference between two dates or times
from datetime import timedelta
"""
-- date, datetime, time and timezone are:
        immutable
        hashalble (can be used as dictionary keys)
        support efficient pickling via pickle module
"""

delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)

print(delta)
# delta.timedelta(days=64, seconds=29156, microseconds=10)


# date Object: represents a date (year, month, and day) in an idealized calendar

"""
datetime.date(year, month, day)
    MINYEAR <= year <= MAXYEAR
    1 <= month <= 12
    1 <= day <= number of days in the given month
"""

from datetime import date

d = date(2002, 12, 31)
d = d.replace(day=26)
print(d)