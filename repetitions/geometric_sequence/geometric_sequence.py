start = float(input())
ratio = float(input())
count = int(input())

term = start
for _ in range(count):
    print(f"{term:.9g}")
    term *= ratio