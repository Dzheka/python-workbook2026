def decimal_to_binary(n):
    if n==0:
        return "0"
    s=""
    while n:
        s+=str(n%2)
        n//=2

    return s[::-1]