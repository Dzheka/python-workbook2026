month = input().lower()

if month in ("january", "march", "may", "july", "august", "october", "december"):
    print("31")
elif month in ("april", "june", "september", "november"):
    print("30")
elif month == "february":
    print("28 or 29")
else:
    print("Invalid month")