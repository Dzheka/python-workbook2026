while True:
    try:
        line = input().strip()
    except EOFError:
        break

    if line == "":
        break

    if len(line) != 8 or not all(c in '01' for c in line):
        print("error")
        continue

    ones = line.count('1')
    if ones % 2 == 0:
        print('0')
    else:
        print('1')
