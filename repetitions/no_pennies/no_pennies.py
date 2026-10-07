total_cents = 0
payment = 0
while True:
    n = input()
    if n == "":
        break
    n = float(n) * 100
    total_cents+=n
print(total_cents / 100)

if total_cents % 5 < 2.5:
    total_cents -= total_cents % 5
else:
    total_cents += 5 - total_cents % 5

print(f"{total_cents/100:.2f}")