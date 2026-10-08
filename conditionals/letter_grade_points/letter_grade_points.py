grade = str(input())

match grade:
    case "A+":
        print(4.0)
    case "A":
        print(4.0)
    case "A-":
        print(3.7)
    case "B+":
        print(3.3)
    case "B":
        print(3.0)
    case "B-":
        print(2.7)
    case "C+":
        print(2.3)
    case "C":
        print(2.0)
    case "C-":
        print(1.7)
    case "D+":
        print(1.3)
    case "D":
        print(1.0)
    case "F":
        print(0.0)
    case _:
        print("Invalid grade")