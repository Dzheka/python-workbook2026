def is_triangle(a,b,c):
    if (a>0 and b>0 and c>0) and (a+b>c and a+c>b and b+c>a):
        return True
    else:
        return False
print (is_triangle(3,4,5))