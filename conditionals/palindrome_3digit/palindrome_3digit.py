n = int(input())

first_digit = n // 100
last_digit = n % 10

if first_digit == last_digit:
    print("palindrome")
else:
    print("not palindrome")