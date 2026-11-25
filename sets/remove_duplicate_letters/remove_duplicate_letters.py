def remove_duplicate_letters(text: str):
    
    b = []

    for i in text:
        if i not in b:
            b.append(i)

    return "".join(b)