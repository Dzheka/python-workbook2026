n = input()
b = 0
while n != "":
    n = float(n)
    b = b + n
    n = input()
pen = b * 100
if pen%5 < 2.5 :
    pen = pen - (pen % 5)
elif pen%5 >= 2.5 :
    pen = pen + (5-(pen%5))
print(f"Total: ${b:.02f}")
print(f"Cash payment: ${(pen/100):.02f}")
