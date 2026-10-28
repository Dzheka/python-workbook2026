t = 0
while True:
    n = input()
    if n == "":
        break
    n = float(n) * 100
    t+=n
print(t / 100)

if t % 5 < 2.5:
    t -= t % 5
else:
    t += 5 - t % 5

print(f"{t/100:.2f}")