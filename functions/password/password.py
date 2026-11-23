import random

def password(length):
    if length < 4:
        return None

    rng = random.SystemRandom()

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    symbols = "!@#$%^&*"

    result = [rng.choice(lower),rng.choice(upper),rng.choice(digits),rng.choice(symbols),]
    characters = lower + upper + digits + symbols

    while len(result) < length:
        result.append(rng.choice(characters))

    rng.shuffle(result)
    return "".join(result)
print(password(8))