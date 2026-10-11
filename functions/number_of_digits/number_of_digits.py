def number_of_digits(n):
    cnt=0
    if n==0:
        return 1
    n=abs(n)
    while n>0:
        cnt+=1
        n//=10
    return cnt

