def first_repeat(x):
    s=set()
    for i in x:
        if i in s:
            return i
        s.add(i)
    return None
def remove_repeats(x):
    s=set()
    r=[]
    for i in x:
        if i not in s:
            s.add(i)
            r.append(i)
    return r