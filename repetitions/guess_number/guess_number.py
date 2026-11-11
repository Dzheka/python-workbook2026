from random import randint
attempts = 0
random = randint(1, 101)
while True:
    guess = int(input())
    attempts += 1
    if guess == random:
        print("Correct!")
        break
    elif guess > random:
        print('Too high')
    elif guess < random:
        print('Too low')
print(attempts)