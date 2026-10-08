a = int(input())
firstd = a//100
secondd = (a//10)%10    
thirdd = a%10
if firstd == thirdd:
    print("Palindrome")
elif firstd != thirdd:
    print("Not Palindrome")
    