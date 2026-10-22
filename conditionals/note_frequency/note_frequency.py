import sys
n = input().lower()
l = n[0]
o = int(n[1])
bf = 0.0
if l == "a" :
    bf = 440.00
elif l == "b":
    bf = 493.88
elif l =="c" :
    bf = 261.63
elif l =="d":
    bf = 293.66
elif l == "e" :
    bf = 329.63
elif l == "f" :
    bf = 349.23
elif l == "g" :
    bf = 392.00
else :
    print("Invalid note")
    sys.exit()

f = bf * (2 ** (o - 4)) 
print(f"{f:.2f}")