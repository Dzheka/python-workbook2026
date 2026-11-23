def encode(text):
    result = ""
    i = 0
    while i < len(text):
        j = i
        while j < len(text) and text[j] == text[i]:
            j += 1
        run = j - i
        if run > 1:
            result += str(run)
        result += text[i]
        i = j
    return result


def decode(code):
    result = ""
    digits = ""
    for ch in code:
        if ch in "0123456789":
            digits += ch
        else:
            count = int(digits) if digits else 1
            result += ch * count
            digits = ""
    return result


def is_worth_it(text):
    return len(encode(text)) < len(text)