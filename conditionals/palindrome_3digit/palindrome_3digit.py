a = int(input())
firstd = a//100
secondd = (a//10)%10    
thirdd = a%10
if firstd == thirdd:
    print("palindrome")
elif firstd != thirdd:
    print("not palindrome")
    