decibels = int(input())

if decibels == 40:
    print("Quiet Room")
elif decibels == 70:
    print("Alarm Clock")
elif decibels == 106:
    print("Gas Lawnmower")
elif decibels == 130:
    print("Jackhammer")
elif decibels < 40:
    print("Quieter than Quiet Room")
elif decibels < 70:
    print("Between Quiet Room and Alarm Clock")
elif decibels < 106:
    print("Between Alarm Clock and Gas Lawnmower")
elif decibels < 130:
    print("Between Gas Lawnmower and Jackhammer")
else:
    print("Louder than Jackhammer")