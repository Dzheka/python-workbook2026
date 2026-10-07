start  = int(input())
diff = int(input())
count = int(input())
print(start)
for i in range(start, start + diff*count - diff, diff):
    print(i + diff)

