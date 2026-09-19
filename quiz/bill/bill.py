price = float(input("subtotal "))
quantity = float(input("discount "))
percent = float(input("total "))
subtotal = price * quantity
discount = subtotal * percent / 100
total = subtotal - discount
print(f"{'subtotal':<10}{subtotal:>6.2f}")
print(f"{'discount':<10}{discount:>6.2f}")
print(f"{'total':<10}{total:>6.2f}")