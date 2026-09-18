"""Read three values with three input() calls — the price of one item, the quantity, and the discount in percent — then print three lines:

subtotal   45.50
discount    2.73
total      42.77
subtotal = price × quantity
discount = the given percent of the subtotal
total = subtotal − discount
Formatting: the label is 10 characters wide and left-aligned, the value is 6 wide, right-aligned, with 2 decimals.

Hint: f"{label:<10}{value:>6.2f}"

Compute the discount from the full subtotal, never from an already rounded number."""

price = float(input())
quantity = int(input())
discount = float(input())

subtotal = price * quantity
discount = subtotal * discount / 100
total = subtotal - discount

print(f"{"subtotal":<10}{subtotal:>6.2f}")
print(f"{"discount":<10}{discount:>6.2f}")
print(f"{"total":<10}{total:>6.2f}")