def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# def day_in_month(month, year):
def days_in_month(month, year):
    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days[month - 1]

def day_of_year(day, month, year):
        s = 0
        for i in range(month, 1, -1):
            s+= days_in_month(i, year)
        return s + day

def weekday(day, month, year):
    if month < 3:
        month += 12
        year -= 1

    q = day
    m = month
    k = year % 100
    j = year // 100

    # using Zeller's formula
    h = (q + ((13 * (m + 1)) // 5) + k + (k // 4) + (j // 4) + (5 * j)) % 7

    weekdays = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return weekdays[h]

def days_between(day1, month1, year1, day2, month2, year2):
    number_d = 0

    if year1 == year2:
        return abs(day_of_year(day2, month2, year2) - day_of_year(day1, month1, year1))

    d_start = 366 if is_leap_year(year1) else 365
    number_d += d_start - day_of_year(day1, month1, year1)

    current_year = year1 + 1
    while current_year < year2:
        if is_leap_year(current_year):
            number_d += 366
        else:
            number_d += 365
        current_year += 1
    n = 0 if is_leap_year(year2) else -1
    number_d += day_of_year(day2, month2, year2)  + n

    return number_d


print(days_between(1, 1, 2026, 12, 10, 2026))  # Expected: 284
print(days_between(12, 10, 2026, 1, 1, 2026))  # Expected: 284
print(days_between(9, 9, 1991, 12, 10, 2026))  # Expected: 12817