a = input().lower()

letter = a[0]
number = int(a[1])

if (letter in "aceg" and number % 2 == 1) or (letter in "bdfh" and number % 2 == 0):
    print("black")
else:
    print("white")