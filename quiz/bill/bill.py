price = float(input())
quantity = int(input())
discount = float(input())
subtotal = price * quantity
price_after_discount = (subtotal * discount) / 100
total = subtotal - price_after_discount
print(f"subtotal: {subtotal:.2f}")
print(f"discount: {price_after_discount:.2f}")
print(f"total: {total:.2f}")
