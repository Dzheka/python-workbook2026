a = float(input())
b = float(input())
c = float(input())
d = a * b
e = d * c / 100
print(f"{'subtotal':<10}{d:>6.2f}")
print(f"{'discount':<10}{e:>6.2f}")
print(f"{'total':<10}{d - e:>6.2f}")