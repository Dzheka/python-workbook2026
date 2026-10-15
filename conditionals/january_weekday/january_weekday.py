from math import floor
year = int(input())

daymap = {
    0: "Saturday",
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday"
}
day = (year + floor((year - 1) / 4) - floor((year - 1) / 100) + floor((year - 1) / 400)) % 7

