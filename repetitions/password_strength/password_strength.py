password = input()
upper = False
lower = False
digit = False
special = False
for char in password:
    if char.isupper():
        upper = True
    if char.islower():
        lower = True
    if char.isdigit():
        digit = True
    if char in "!@#$%^&*()-_+=[]{}|;:,.<>?":
        special = True
score = 0
if upper:
    score += 1
if lower:
    score += 1
if digit:
    score += 1
if special:
    score += 1
if len(password) >= 8:
    score += 1
if score <= 1:
    print("Very Weak")
elif score == 2:
    print("Weak")
elif score == 3:
    print("Medium")
elif score == 4:
    print("Strong")
else:
    print("Very Strong")