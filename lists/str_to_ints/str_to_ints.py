def str_to_ints(x: str) ->list[int]:
    s=[]
    if x=="":
        return []
    else:
        a=x.split()
        for i in range (len(a)):
            s.append(int(a[i]))
        return s    

print(str_to_ints("2 3 5 7 11"))
print(str_to_ints("10 -5 3"))
print(str_to_ints(""))