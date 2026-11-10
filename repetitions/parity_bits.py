import sys

lines = sys.stdin.read().splitlines()
for line in lines:
    line = line.strip()
    if not line:
        continue
    if len(line) != 8 or not all(c in '01' for c in line):
        print("error")
        continue
    ones = line.count('1')
    print('0' if ones % 2 == 0 else '1')
