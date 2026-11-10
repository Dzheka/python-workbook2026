def binomial(n, k):
    if k < 0 or k > n:
        return 0
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i
    return result
def pascal_row(n):
    return " ".join(str(binomial(n, k)) for k in range(n + 1))


def pascal_triangle(rows):
    if rows <= 0:
        return ""
    width = len(pascal_row(rows - 1))
    lines = []
    for n in range(rows):
        row = pascal_row(n)
        lines.append(" " * ((width - len(row)) // 2) + row)
    return "\n".join(lines)

print(pascal_triangle(10))