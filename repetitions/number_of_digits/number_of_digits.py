a = abs(int(input()))
count = 0
while a >0:
    count+=1
    a = a//10
if count==0:
 count = 1
print(count)