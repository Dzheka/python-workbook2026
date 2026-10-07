level = float(input())

if level < 40:
    print("Quieter than Quiet Room")
elif level == 40:
    print("Quiet Room")
elif level < 70:
    print("Between Quiet Room and Alarm Clock")
elif level == 70:
    print("Alarm Clock")
elif level < 106:
    print("Between Alarm Clock and Gas Lawnmower")
elif level == 106:
    print("Gas Lawnmower")
elif level < 130:
    print("Between Gas Lawnmower and Jackhammer")
elif level == 130:
    print("Jackhammer")
else:
    print("Louder than Jackhammer")