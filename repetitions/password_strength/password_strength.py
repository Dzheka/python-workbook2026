met = 0
password = input()

for i in password:
    if i.isdigit():
        met+= 1
        break
for i in password:
    if i in "!@#$%^&*()_+-=[]{}|;:,.<>?":
        met += 1
        break
for i in password:
    if i.islower():
        met += 1
        break
for i in password:
    if i.isupper():
        met+=1
        break
if len(password) >= 8:
    met += 1

levels = ["Very Weak", "Very Weak", "Weak", "Medium", "Strong", "Very Strong"]
print(levels[met])