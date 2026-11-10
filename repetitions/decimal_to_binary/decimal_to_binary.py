n = int(input())
a = ''

while True:
    b = n % 2
    a = str(b) + a
    n = n // 2
    if n == 0:
        print(a)
        break