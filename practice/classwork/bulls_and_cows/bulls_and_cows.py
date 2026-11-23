def is_valid_secret(code):
    if len(code) != 4 or not code.isdigit() or code[0] == "0":
        return False
    for i in range(4):
        for j in range(i + 1, 4):
            if code[i] == code[j]:
                return False
    return True


def bulls(secret, guess):
    count = 0
    for i in range(4):
        if secret[i] == guess[i]:
            count += 1
    return count


def cows(secret, guess):
    count = 0
    for i in range(4):
        if secret[i] != guess[i] and guess[i] in secret:
            count += 1
    return count


def score(secret, guess):
    if not is_valid_secret(guess):
        return "invalid"
    b = bulls(secret, guess)
    if b == 4:
        return "win"
    return f"{b}B{cows(secret, guess)}C"


if __name__ == "__main__":
    secret = "5823"
    while True:
        guess = input("Your guess: ")
        result = score(secret, guess)
        print(result)
        if result == "win":
            break
