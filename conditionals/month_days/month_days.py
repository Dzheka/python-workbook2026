month = input().lower()

if month == "february":
    print("28 or 29")
elif month == "april" or month == "june" or month == "september" or month == "november":
    print("30")
elif (month == "january" or month == "march" or month == "may"
      or month == "july" or month == "august" or month == "october"
      or month == "december"):
    print("31")
else:
    print("Invalid month")