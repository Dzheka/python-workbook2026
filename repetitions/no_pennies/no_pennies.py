total = 0
while True:
    price = input()
    if price == "":
        break
    total += float(price)
cash = round(total / 0.05) * 0.05
print(f"Total: ${total:.2f}")
print(f"Cash payment: ${cash:.2f}")