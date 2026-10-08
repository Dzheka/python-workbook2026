a= int(input())
firstd = a//1000
secondd = (a//100)%10
thirdd = (a//10)%10
fourthd = a%10
if firstd == fourthd and secondd == thirdd:
    print("Palindrome") 
else :
    print("Not Palindrome")
    