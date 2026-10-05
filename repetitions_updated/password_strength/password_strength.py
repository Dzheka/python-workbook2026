password = input()

has_upper = False
has_lower = False
has_digit = False
has_special = False

special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in special_chars:
        has_special = True

has_length = len(password) >= 8

# Count criteria met
criteria_met = 0
if has_upper:
    criteria_met += 1
if has_lower:
    criteria_met += 1
if has_digit:
    criteria_met += 1
if has_special:
    criteria_met += 1
if has_length:
    criteria_met += 1

if criteria_met <= 1:
    print("Very Weak")
elif criteria_met == 2:
    print("Weak")
elif criteria_met == 3:
    print("Medium")
elif criteria_met == 4:
    print("Strong")
else:
    print("Very Strong")
