start = float(input())
ratio = float(input())
count = int(input())

current = start
for _ in range(count):
    print(f"{current:.9g}")
    current *= ratio
