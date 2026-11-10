special = set("!@#$%^&*()_+-=[]{}|;:,.<>?")
password = input()

score = sum([
    any(c.isupper() for c in password),
    any(c.islower() for c in password),
    any(c.isdigit() for c in password),
    any(c in special for c in password),
    len(password) >= 8,
])

levels = ["Very Weak", "Very Weak", "Weak", "Medium", "Strong", "Very Strong"]
print(levels[score])