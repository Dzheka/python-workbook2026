"""
The length of a month varies from 28 to 31 days. Create a program that reads the name of a month from the user as a string and displays the number of days in that month.

Month Days
Month	Days
January	31
February	28 or 29
March	31
April	30
May	31
June	30
July	31
August	31
September	30
October	31
November	30
December	31
"""

days = ['31', '28 or 29', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',	'november',
          'december']
month = input().lower()

if month in months:
    i = months.index(month)
    print(days[i])
else:
    print('Invalid month')

