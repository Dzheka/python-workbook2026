def in_both(x,y):
    return list(sorted(set(x) & set(y)))
def in_exactly_one(x,y):
    return list(sorted(set(x) ^ set(y)))
def in_neither(a,x,y):
    return list(sorted(set(a)-(set(x) | set(y))))
print(in_neither(["Ali", "Bek", "Madina", "Nilu", "Sara", "Timur"], ["Ali", "Nilu", "Sara"], ["Bek", "Sara", "Ali"]))