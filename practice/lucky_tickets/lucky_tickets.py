a=int(input())
b=int(input())
count = 0
def digit_sum(n):
    sum = 0
    while n>0:
        sum= sum+n%10
        n=n//10
    return sum
def is_lucky(x):
    if digit_sum(x//1000) == digit_sum(x%1000):
        return True 
    else:
        return False
for x in range (a, b+1):
    if is_lucky(x) == True:
        count+=1
print(count)
