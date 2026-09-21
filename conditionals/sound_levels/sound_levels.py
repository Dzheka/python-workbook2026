a = int(input())
if a==40:
    print("Quiet Room")
elif 40<a<70:
    print("Between Quiet Room and Alarm Clock")
elif a==70:
    print("Alarm Clock")
elif 70<a<106:
    print("Between Alarm Clock and Gas Lawnmower")
elif a==106:
    print("Gas Lawnmower")
elif 106<a<130:
    print("Between Gas Lawnmower and Jackhammer")
elif a == 130:
    print ("Jackhammer")
elif a>130:
    print("Louder than Jackhammer")
elif a<40:
    print("Quieter than Quiet Room")
else :
    print ("Unknown status code")