# Print each row of the multiplication table
for row in range(1, 10):
    for col in range(1, 10):
        product = row * col
        print(f"{product:2}", end=" ")
    print()
