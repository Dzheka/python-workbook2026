# Read number from user
x = float(input())

# Initialize guess
guess = x / 2

# Loop until guess is good enough
while abs(guess * guess - x) > 1e-12:
    # Update guess using Newton's method
    guess = (guess + x / guess) / 2

# Display result
print(guess)
