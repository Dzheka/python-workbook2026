"""Write a program that determines the
 day of the week for January 1st of a given year using a mathematical formula.

Formula
day_of_week = (year + floor((year - 1) / 4) -
floor((year - 1) / 100) + floor((year - 1) / 400)) % 7"""

days = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
]

year = int(input())

day_index = (
    year + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400
) % 7

print(days[day_index])