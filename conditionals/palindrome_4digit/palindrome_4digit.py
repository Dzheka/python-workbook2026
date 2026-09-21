a = int(input())
b = a//1000
c = (a//100)%10
d = (a//10)%10
e = a % 10
if b == e and c == d:
    print("palindrome") 
else :
    print("not palindrome")