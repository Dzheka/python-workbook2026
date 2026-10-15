"""Logic
If n > 0: positive
If n < 0: negative
If n == 0: zero
Note
Handle integer input
Zero is neither positive nor negative
Use simple comparison operators"""

n = int(input())

if n > 0:
    print("positive")
elif n < 0:
    print("negative")
else:
    print("zero")