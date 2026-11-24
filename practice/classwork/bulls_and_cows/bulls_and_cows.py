def is_valid_secret(code):
    s = str(code)
    if len(set(s)) == 4 and s[0] != '0' and s.isdigit():
        return True
    else:
        return False

def bulls(secret, guess):
    n = 0
    c = 0
    while c < 4:
        if secret[c] == guess[c]:
            n+=1
        c+=1
    return n

def cows(secret, guess):
    n = 0
    c = 0
    while c < 4:
        if secret[c] == guess[c]:
            c+=1
            continue
        elif secret[c] in guess:
            n+=1
        c+=1
    return n

def score(secret, guess):
    if  not (is_valid_secret(secret) and is_valid_secret(guess)):
        return 'invalid'

    b = bulls(secret, guess)
    c = cows(secret, guess)

    if  b == 4:
        return 'win'

    return f"{b}B{c}C"





