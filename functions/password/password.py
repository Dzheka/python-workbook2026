from random import choice
def password(length):
    word = ''
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?"
    for i in range(1, length + 1):
        word += choice(chars)
    return word
print(password(7))