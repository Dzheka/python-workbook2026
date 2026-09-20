magnitude = float (input())
if magnitude <2:
    print ("Micro")
elif 2.0 <= magnitude < 3.0:
    print ("Very Minor")
elif 3.0 <= magnitude < 4.0:
    print ("Minor")
elif 4.0 <= magnitude < 5.0:
    print ("Light")
elif 5.0 <= magnitude < 6.0:
    print ("Moderate")
elif 6.0 <= magnitude < 7.0:
    print ("Strong")
elif 7.0 <= magnitude < 8.0:
    print ("Major")
elif 8.0 <= magnitude < 10.0:
    print ("Great")
elif magnitude >= 10.0:
    print ("Meteoric")
