number = int(input())
d = number//86400
h = (number%86400)//3600
m = (number % 3600)//60
s = number % 60
print(f"{d}:{h:02}:{m:02}:{s:02}")

