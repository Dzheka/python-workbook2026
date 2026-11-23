def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False
print(is_triangle(1,2,3))