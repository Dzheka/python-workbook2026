sound_lvls = int(input())

if sound_lvls == 40:
    print("Quiet Room")
elif sound_lvls < 40:
    print("Quieter than Quiet Room")
elif 40 < sound_lvls < 70:
    print("Between Quiet Room and Alarm Clock")
elif sound_lvls == 70:
    print("Alarm Clock")
elif 70 < sound_lvls < 106:
    print("Between Alarm Clock and Gas Lawnmower")
elif sound_lvls == 106:
    print("Gas Lawnmower")
elif 106 < sound_lvls < 130:
    print("Between Gas Lawnmower and Jackhammer")
elif sound_lvls == 130:
    print("Jackhammer")
else:
    print("Louder than Jackhammer")