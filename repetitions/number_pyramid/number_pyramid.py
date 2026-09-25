n = int(input())


# print spaces how much?
# print numbers what  numbers? how much numbers?
# print \n and move to the next interation
for row in range(1, n + 1 ):
#    print(row, end=" ")
    for i in range(1, n - row + 1):
        print(end=" ")
#    if row == 1:
#       print("1")
    for i in range(1, row + 1):
        print(i, end='')
    for i in range(row - 1, 0, -1):
        print(i, end="")
    print(end='\n')