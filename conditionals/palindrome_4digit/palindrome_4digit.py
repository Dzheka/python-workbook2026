number = int(input())
first = number // 1000
second = (number // 100) % 10
third = (number // 10) % 10
last = number % 10

if first == last and second == third:
    print("palindrome")
else:
    print("not palindrome")
