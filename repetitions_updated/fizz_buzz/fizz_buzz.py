# Loop from 1 to 100
for i in range(1, 101):
    # Check if divisible by both 3 and 5 (15)
    if i % 15 == 0:
        print("fizzbuzz")
    # Check if divisible by 3
    elif i % 3 == 0:
        print("fizz")
    # Check if divisible by 5
    elif i % 5 == 0:
        print("buzz")
    # Otherwise print the number
    else:
        print(i)
