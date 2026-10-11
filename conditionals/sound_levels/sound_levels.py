n=int(input())
if n<40 :
    print("Quieter than Quiet Room")
elif n==40:
    print("Quiet Room")
elif n>40 and n<70 :
    print("Between Quiet Room and Alarm Clock")
elif n==70:
    print("Alarm Clock")
elif n>70 and n<106 :
    print("Between Alarm Clock and Gas Lawnmower")
elif n==106:
    print("Gas Lawnmower")
elif n>106 and n<130:
    print("Between Gas Lawnmower and Jackhammer")
elif n==130 :
    print("Jackhammer")
else :
    print("Louder than Jackhammer")

#Between Gas Lawnmower and Jackhammer