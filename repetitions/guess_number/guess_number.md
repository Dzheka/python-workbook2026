# Guess the Number

A number guessing game where the computer picks a number and gives hints.

## Task
- Computer picks a random number between 1 and 100
- User tries to guess the number
- After each guess, provide feedback:
  - "Too low" if guess is less than the number
  - "Too high" if guess is greater than the number
  - "Correct!" when guessed correctly
- Display the number of attempts taken

## Example Session
```
Guess a number between 1 and 100: 50
Too low
Guess a number between 1 and 100: 75
Too high
Guess a number between 1 and 100: 62
Too low
Guess a number between 1 and 100: 68
Correct! You guessed it in 4 attempts
```

## Logic
- Use `random.randint(1, 100)` to pick a number
- Initialize attempt counter to 0
- Use a while loop:
  - Read user's guess
  - Increment attempt counter
  - Compare guess with target:
    - If less: display "Too low"
    - If greater: display "Too high"
    - If equal: display success message and break
- Display number of attempts

## Hint
```python
import random
target = random.randint(1, 100)
```
