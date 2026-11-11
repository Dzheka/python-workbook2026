a=float(input())
if a==40:
    print("Quiet Room")
elif a==70:
    print("Alarm Clock")
elif a==106:
    print("Gas Lawnmower")
elif a==130:
    print("Jackhammer")
elif a<40:
    print ("Quieter than Quiet Room")
elif a<70:
    print ("Between Quiet Room and Alarm Clock")
elif a<106:
    print("Between Alarm Clock and Gas Lawnmower")
elif a<130:
    print("Between Gas Lawnmower and Jackhammer")
else:
    print("Louder than Jackhammer")