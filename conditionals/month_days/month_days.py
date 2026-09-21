a = input()
if a == "January" or a == "March" or a == "May" or a == "July" or a == "August" or a == "October" or a == "December" or a=="DECEMBER":
    print("31")
elif a == "April" or a == "June" or a == "September" or a == "November":
    print("30")
elif a == "February" or a == "february" :
    print("28 or 29")
else :
    print("Invalid month")