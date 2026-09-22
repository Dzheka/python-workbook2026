a = float(input())
b = int(input())
c = int(input())

discount = a * b * c / 100
total = a * b - discount

print(f"{'subtotal':<9}{a * b:>7.2f}")
print(f"{'discount':<9}{discount:>7.2f}")
print(f"{'total':<9}{total:>7.2f}")
