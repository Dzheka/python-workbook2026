name = str(input())
name = name.lower()


match name:
    case "january":
        print(31)
    case "february":
        print("28 or 29")
    case "march":
        print(31)
    case "april":
        print(30)
    case "may":
        print(31)
    case "june":
        print(30)
    case "july":
        print(31)
    case "august":
        print(31)
    case "september":
        print(30)
    case "october":
        print(31)
    case "november":
        print(30)
    case "december":
        print(31)
    case _:
        print("Invalid month")