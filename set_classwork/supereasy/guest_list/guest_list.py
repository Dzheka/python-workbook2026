def add_guests(a, b):
    a=set(a)
    b=set(b)
    c=a|b
    c=list(c)
    return c
def remove_guests(a, b):
    a=set(a)
    b=set(b)
    c=a-b
    c=list(c)
    return c