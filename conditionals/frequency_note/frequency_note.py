a=int(input())
if a>= 261.63 and a<293.66 :
    print("C4")
elif  a>=293.66  and  a<329.63   :
    print("D4")
elif  a>=329.63  and  a<349.23   :
    print("E4")
elif  a>=349.23  and  a<392.00   :
    print("F4")
elif  a>=392.00  and  a<440.00   :
    print("G4")
elif  a>=440.00  and  a<493.88   :
    print("A4")
elif  a==493.88   :
    print("B4")
else :
    print("No match")