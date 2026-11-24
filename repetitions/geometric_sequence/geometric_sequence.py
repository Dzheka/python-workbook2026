start = float(input())
ratio = float(input())
count = int(input())

# print start
# print start * ratio
# print start * ratio ** i
# keep printing until i > count
i = 1
print(int(start))
while i < count:
    a = start * ratio ** i
    print(f"{a}".rstrip('0').rstrip('.'))
    i = i + 1