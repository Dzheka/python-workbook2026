def gregorian_to_ordinal(year: int, month: int, day: int) -> int:
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    days_in_months = [31, 29 if is_leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    return sum(days_in_months[:month - 1]) + day
