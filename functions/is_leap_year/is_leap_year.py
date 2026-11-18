def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

"""user_input = int(input())
if is_leap_year(user_input):
    print("Leap year")
else:
    print("Not leap year")"""