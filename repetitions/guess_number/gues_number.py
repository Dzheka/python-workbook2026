import random
randn = random.randint(1, 100)
sum = 0
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    sum += 1
    if guess < randn:
        print("Too low")
    elif guess > randn:
        print("Too high")
    else:
        print(f"Correct! You guessed it in {sum} attempts")
        break