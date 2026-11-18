year = ["Invalid year", 'Freshman', 'Sophomore', 'Junior', 'Senior']

i = int(input())

if i <= len(year) - 1 and (i > 0):
    print(year[i])
else:
    print(year[0])

