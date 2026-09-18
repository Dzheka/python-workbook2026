decibels = float(input("Enter the sound level in decibels (dB): "))

if decibels < 40:
    print("Quieter than Quiet Room")
elif decibels == 40:
    print("Quiet Room")
elif 40 < decibels < 70:
    print("Between Quiet Room and Alarm Clock")
elif decibels == 70:
    print("Alarm Clock")
elif 70 < decibels < 106:
    print("Between Alarm Clock and Gas Lawnmower")
elif decibels == 106:
    print("Gas Lawnmower")
elif 106 < decibels < 130:
    print("Between Gas Lawnmower and Jackhammer")
elif decibels == 130:
    print("Jackhammer")
else:
    print("Louder than Jackhammer")