def ordinal_to_gregorian(year, day_of_year):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        days[1] = 29

    month = 1

    while day_of_year > days[month - 1]:
        day_of_year -= days[month - 1]
        month += 1

    return (year, month, day_of_year)
print(ordinal_to_gregorian(2024, 32))