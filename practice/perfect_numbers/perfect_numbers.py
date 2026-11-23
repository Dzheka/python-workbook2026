a=int(input())
b=int(input())
def sum_of_divisors(n):
    sum = 0
    for i in range (1, n):
        if n%i==0:
            sum=sum+i
    return sum
q=0
e=0
w=0
def classify(n):
    global q,w,e
    if sum_of_divisors(n) == n:
        q=q+1
        return "perfect"
    elif sum_of_divisors(n)>n:
        e=e+1
        return "abundant"
    else:
        w=w+1
        return "deficient"
for x in range (a, b+1):
    d = classify(x)
    print(f"{x} is {d}")
print(f"Perfect: {q}, Abundant: {e}, Deficient: {w}")



    

