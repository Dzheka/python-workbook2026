n = int(input())

match n:
    case 1:
        print("Freshman")
    case 2:
        print("Sophomore")
    case 3:
        print("Junior")
    case 4:
        print("Senior")
    case _:
        print("Invalid year")
