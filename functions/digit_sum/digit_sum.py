def digit_sum(n):
    cnt=0
    if n==0:
        return 0
    n=abs(n)
    while n>0:
        cnt+=n%10
        n//=10
    return cnt

