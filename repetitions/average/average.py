b = 1
a = 0
c = 0
while b>0:
    b = int(input())
    a += b
    c += 1
print(f"The average is {(a/(c-1)):.1f}")