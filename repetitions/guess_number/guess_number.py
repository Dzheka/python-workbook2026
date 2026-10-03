import random
target = random.randint(1, 100)
attempts = 0
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1
    if guess < target:
        print("Too low")
    elif guess > target:
        print("Too high")
    else:
        print(f"Correct! You guessed it in {attempts} attempts")
        break