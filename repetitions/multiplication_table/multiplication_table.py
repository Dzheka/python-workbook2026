for j in range(1, 10):
    for i in range(1, 10):
        if i * j > 9:
            print(i * j, end=' ')
        else:
            print(i * j, end='  ')
    print()
