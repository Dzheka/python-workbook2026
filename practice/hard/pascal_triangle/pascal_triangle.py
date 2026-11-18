def binomial(n, k):
    if k < 0 or k > n:
        return 0

    a = 1
    for i in range(1, k + 1):
        a = a * (n - i + 1) // i
    return a

def pascal_row(n):
    b = ""
    for k in range(n + 1):
        if k > 0:
            b += " "
        b += str(binomial(n, k))
    return b

def pascal_triangle(rows):
    if rows <= 0:
        return ""

    x = len(pascal_row(rows - 1))
    c = ""

    for n in range(rows):
        row = pascal_row(n)
        if n > 0:
            c += "\n"
        c += " " * ((x - len(row)) // 2) + row

    return c   