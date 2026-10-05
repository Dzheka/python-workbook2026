year = int(input())

day_of_week = (
    year
    + (year - 1) // 4
    - (year - 1) // 100
    + (year - 1) // 400
) % 7

days = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]

print(days[day_of_week])