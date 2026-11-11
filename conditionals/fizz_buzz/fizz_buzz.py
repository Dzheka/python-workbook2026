"""Fizz Buzz
Write a program that implements the FizzBuzz logic for a single number.

FizzBuzz Rules
If divisible by 3 only: "Fizz"
If divisible by 5 only: "Buzz"
If divisible by both 3 and 5: "FizzBuzz"
Otherwise: display the number itself"""

i = int(input())

if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
elif i % 5 == 0:
    print("Buzz")
elif i % 3 == 0:
    print("Fizz")
else:
    print(i)