number = int(input())
first = number // 100
last = number % 10

if first == last:
    print("palindrome")
else:
    print("not palindrome")
