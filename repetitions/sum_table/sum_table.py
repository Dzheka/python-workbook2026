for j in range(0, 10):
    for i in range(0 + j, 10 + j):
        if i >= 10:
            print(f'{i}', end=' ')
        else:
            print(f'{i}', end='  ')
    print(end='\n')