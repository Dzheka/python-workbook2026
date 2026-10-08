import datetime

year = int(input())
month = int(input())
day = int(input())

today = datetime.date(year, month, day)
tomorrow = today + datetime.timedelta(days=1)
print(tomorrow.year, tomorrow.month, tomorrow.day)