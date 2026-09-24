c = []
a = 0

while True:
    i = int(input())
    if i == 0:
        break
    c.append(i)

for i in c:
    a += i
print(f"The average is {(a/len(c)):.1f}")
