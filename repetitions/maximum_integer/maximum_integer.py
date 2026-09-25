from random import randint
c = 0
r = randint(1, 101)
print(r)
max = r
for  i in range(1, 100):
    row  = ''
    r = randint(1, 101)
    row += str(r)
    if r > max:
        max = r
        c += 1
        row+=' <== Update'
    print(row)
print('maximum', max)
print(c)
