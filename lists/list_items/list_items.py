def first_item(x):
    return x[0]
def last_item(x):
    return x[-1]
def mid_item(x):
    d=len(x)//2
    return x[d]
items = [2, 3, 7, 11]
print(first_item(items))
print(mid_item(items))   
print(last_item(items))  