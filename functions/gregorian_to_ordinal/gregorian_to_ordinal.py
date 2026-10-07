def gregorian_to_ordinal(year, month, day):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        days[1] = 29

    result = day

    for i in range(month - 1):
        result += days[i]

    return result
print(gregorian_to_ordinal(2024, 1, 1))