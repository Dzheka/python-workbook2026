from random import choice

def password(length):
    word = ''
    chars = "abcdefghijklmnopqrstuvwxyz"
    upper_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    numbers = "0123456789"
    special_chars = "!@#$%^&*()"
    for i in range(1, length - 2):
        word += choice(chars)
    word += choice(upper_chars)
    word += choice(numbers)
    word+= choice(special_chars)
    return word
print(password(20))