number = int(input())

first_digit = number // 100
last_digit = number % 10

if first_digit == last_digit:
    print("palindrome")
else:
    print("not palindrome")