from random import randint
c = 0
r = randint(1, 101)
print(r)
m = r
for  i in range(1, 100):
    a  = ''
    r = randint(1, 101)
    a += str(r)
    if r > m:
        m = r
        c += 1
        a+=' <== Update'
    print(a)
print('maximum', m)
print(c)