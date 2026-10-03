start = float(input())
ratio = float(input())
count = int(input())
for i in range(count):
    print(f"{start:.9g}")
    start = start * ratio
