import random

target = random.randint(1, 100)

while True:
    guess = int(input())

    if guess < target:
        print("Too low")
    elif guess > target:
        print("Too high")
    else:
        print("Correct")
        break
