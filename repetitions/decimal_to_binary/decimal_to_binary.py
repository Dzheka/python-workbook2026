q = int(input())
res = ""
if q == 0:
    res = 0
while q > 0:
    r = q % 2
    res = str(r) + res
    q = q // 2
print(f"The binary equivalent is {res}")