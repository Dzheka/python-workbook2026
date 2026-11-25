def progress_bar(a,b):
    if a<0:
        P=0
        p=0
    elif a>=100:
        P=100
        p=b
    else:
        P=a
        p=int(a/100*b)
    return f"[{"#" * p}{"-" * (b-p)}] {P}%"
print (progress_bar(99, 10))
    