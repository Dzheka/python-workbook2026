x = float(input())

guess = x / 2

while abs(guess * guess - x) > 1e-12:
    # Update guess using Newton's method
    guess = (guess + x / guess) / 2

print(guess)
