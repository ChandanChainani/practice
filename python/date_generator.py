def get_date(year, end_range):
    from datetime import datetime

    JAN, FEB, MAR, APR, MAY, JUN, JULY, AUG, SEP, OCT, NOV, DEC = (
        1,  2,  3,
        4,  5,  6,
        7,  8,  9,
        10, 11, 12
    )
    day, month = 1, JAN
    MONTHS_OF_30_DAYS = {APR, JUN, SEP, NOV}
    for _ in range(end_range):
        yield datetime(day=day, month=month, year=year).date()

        day += 1

        if (
            day > 31
            or (month == FEB and day > (29 if year % 4 == 0 else 28))
            or (day > 30 and month in MONTHS_OF_30_DAYS)
        ):
            day = 1
            month += 1

        if month > DEC:
            month = JAN
            year += 1

# for date in get_date(2018, 365):
#     print(date)

TOTAL_DAYS_IN_YEAR = 365

IDX = 1
YEAR = 2018
for date in get_date(YEAR, TOTAL_DAYS_IN_YEAR * 3 + 1):
# for idx, date in enumerate(get_date(YEAR, 36)):
# for idx, date in enumerate(get_date(YEAR, 367)):
    if IDX > (TOTAL_DAYS_IN_YEAR + (1 if YEAR % 4 == 0 else 0)):
        YEAR += 1
        IDX = 1
    print("{}: {}".format(str(IDX).rjust(3, "0").ljust(4, " "), date))
    IDX += 1
