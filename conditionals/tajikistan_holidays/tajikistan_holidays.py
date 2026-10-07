"""Write a program that reads a date (month and day) from the user and determines if it corresponds to a national holiday in Tajikistan.

Tajikistan National Holidays Reference Table
Date	Holiday Name
January 1	New Year's Day
March 8	International Women's Day
March 21-24	Navruz (Persian New Year)
May 1	Labour Day
May 9	Victory Day
June 27	National Unity Day
September 9	Independence Day
November 6	Constitution Day"""

month = int(input())
day = int(input())

if month == 1 and day == 1:
    print("New Year's Day")
elif month == 3 and day == 8:
    print("International Women's Day")
elif month == 3 and 21 <= day <= 24:
    print("Navruz (Persian New Year)")
elif month == 5 and day == 1:
    print("Labour Day")
elif month == 5 and day == 9:
    print("Victory Day")
elif month == 6 and day == 27:
    print("National Unity Day")
elif month == 9 and day == 9:
    print("Independence Day")
elif month == 11 and day == 6:
    print("Constitution Day")
else:
    print("Not a national holiday")