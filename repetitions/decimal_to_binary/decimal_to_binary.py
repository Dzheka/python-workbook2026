n = int(input())
res = ''

while True:
    r = n % 2
    res = str(r) + res
    n = n // 2
    if n == 0:
        print(res)
        break
