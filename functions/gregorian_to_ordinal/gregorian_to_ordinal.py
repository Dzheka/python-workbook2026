def gregorian_to_ordinal(year, month, day):
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    if is_leap:
        days_in_months[1] = 29

    return sum(days_in_months[: month - 1]) + day