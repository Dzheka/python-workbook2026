# Password Strength

Evaluate password strength based on character types, length, and special characters.

## Task
- Read a password from the user
- Check for five criteria:
  - Contains at least one uppercase letter
  - Contains at least one lowercase letter
  - Contains at least one digit
  - Contains at least one special character `!@#$%^&*()_+-=[]{}|;:,.<>?`
  - Password length is at least 8 characters
- Display the strength level based on criteria met:
  - **Very Weak**: 1 criteria met
  - **Weak**: 2 criteria met
  - **Medium**: 3 criteria met
  - **Strong**: 4 criteria met
  - **Very Strong**: 5 criteria met (all criteria)

## Examples
**Example 1:**
```
Hello123!@#
```
```
Very Strong
```

**Example 2:**
```
Hello123
```
```
Strong
```

**Example 3:**
```
hello123
```
```
Weak
```

**Example 4:**
```
hello
```
```
Very Weak
```

**Example 5:**
```
12345
```
```
Very Weak
```

**Example 6:**
```
Hel!23
```
```
Medium
```
