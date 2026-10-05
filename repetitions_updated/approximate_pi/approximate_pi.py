# Initialize approximation with the first term
approximation = 3.0

# Display first approximation
print(f"Approximation 1: {approximation}")

# Calculate and display 14 more approximations
for i in range(2, 16):
    # Calculate the denominator: n, n+1, n+2 where n increases by 2 each time
    n = (i - 1) * 2
    denominator = n * (n + 1) * (n + 2)

    # Alternate between adding and subtracting
    if i % 2 == 0:
        approximation += 4 / denominator
    else:
        approximation -= 4 / denominator

    print(f"Approximation {i}: {approximation}")
