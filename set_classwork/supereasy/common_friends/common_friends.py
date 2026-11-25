def common(a: list, b: list):
    a=set(a)
    b=set(b)
    c=a&b
    c=list(c)
    return c
def only_first(a: list, b: list):
    a=set(a)
    b=set(b)
    c = a - b
    c=list(c)
    return c
print(common(["Bek", "Nilu", "Timur"], ["Nilu", "Bek"]))
print(only_first(["Bek", "Nilu", "Timur"], ["Nilu", "Bek"]))