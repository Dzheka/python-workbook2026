def list_to_string(w: list[str]):
    if w==[]:
        return ""
    else:
        s=w[0]
        for i in range (1, len(w)):
            s = s + " " + w[i]
    return s
print(list_to_string(["Hello", "world"]))
print(list_to_string(["Python", "is", "fun"]))
print(list_to_string([]))