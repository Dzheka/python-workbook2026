n = int(input())

match n:
    case 3:
        print("Triangle")
    case 4:
        print("Quadrilateral")
    case 5:
        print("Pentagon")
    case 6:
        print("Hexagon")
    case 7:
        print("Heptagon")
    case 8:
        print("Octagon")
    case 9:
        print("Nonagon")
    case 10:
        print("Decagon")
    case _:
        print("Invalid number of sides")
