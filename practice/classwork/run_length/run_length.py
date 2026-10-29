def encode(text):
    a = ""
    i = 0
    while i < len(text):
        k = 1
        while i + k < len(text) and text[i] == text[i + k]:
            k += 1
        if k > 1:
            a += str(k)
        a += text[i]
        i += k
    return a

def decode(code):
    b = ""
    c = ""
    for char in code:
        if char in "0123456789":
            c += char
        else:
            if c != "":
                count = int(c)
            else:
                count = 1
            b += char * count
            c = ""
    return b

def is_worth_it(text):
    return len(encode(text)) < len(text)