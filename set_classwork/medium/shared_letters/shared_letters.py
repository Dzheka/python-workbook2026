def common_letters(x):
    b=set()
    if not x:
        return []
    a=set(c.lower() for c in x[0] if c.isalpha())
    for i in x[1:]:
        a=a&set(c.lower() for c in i if c.isalpha())
    return sorted(a)
def any_letters(x):
    a=set()
    for i in x:
        a=a|set(c.lower() for c in i if c.isalpha())
    return sorted(a)