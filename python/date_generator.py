def get_date(limit):
    from datetime import datetime

    JAN, FEB, MAR, APR, MAY, JUN, JULY, AUG, SEP, OCT, NOV, DEC = (
        1,  2,  3,
        4,  5,  6,
        7,  8,  9,
        10, 11, 12
    )
    TOTAL_DAYS_IN_YEAR = 365
    day, month, year, days_counter = 1, JAN, 1990, 1
    i = 0
    while i < limit:
        yield datetime(day=day, month=month, year=year).date()

        day += 1
        days_counter += 1

        if (
            day > 31
            or (month == FEB and day > 28)
            or (day > 30 and month in [APR, JUN, SEP, NOV])
        ):
            day = 1
            month += 1

        if month > DEC:
            month = JAN

        if days_counter == TOTAL_DAYS_IN_YEAR:
            days_counter = 0
            year += 1

        i += 1


# for date in get_date(365):
#     print(date)


# for idx, date in enumerate(get_date(365 * 3)):
# for idx, date in enumerate(get_date(365)):
for idx, date in enumerate(get_date(36)):
    print("{}: {}".format(str(idx + 1).rjust(3, "0").ljust(4, " "), date))
