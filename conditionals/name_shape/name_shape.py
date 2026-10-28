a=int(input())

shape = {
    3: "Triangle",
    4: "Quadrilateral",
    5: "Pentagon",
    6: "Hexagon", 
    7: "Heptagon",
    8: "Octagon",
    9: "Nonagon",
    10: "Decagon"
}
if a in shape:
    print(shape[a])
else:
    print("Invalid number of sides")