n = int(input())
guess = n /2
while abs(guess ** 2 - n) > 1e-12:
    guess = (guess + n / guess) / 2
print(round(guess, 10))