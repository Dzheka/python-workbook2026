height = int(input()) + 1
c = 0
for i in range(1, height):
    row = ''
    row += (height - i - 1) * ' '
    row += (2 * i - 1) * '*'
    print(row)