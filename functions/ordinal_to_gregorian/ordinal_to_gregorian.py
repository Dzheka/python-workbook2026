def ordinal_to_gregorian(year: int, day_of_year: int) -> tuple[int, int, int]:
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    days_in_months = [31, 29 if is_leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    month = 1
    for days in days_in_months:
        if day_of_year <= days:
            break
        day_of_year -= days
        month += 1
        
    return (year, month, day_of_year)
