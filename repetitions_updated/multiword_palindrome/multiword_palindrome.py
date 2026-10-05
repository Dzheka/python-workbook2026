# Read string from user
string = input()

# Remove spaces and convert to lowercase
cleaned = ""
for char in string:
    if char.isalnum():
        cleaned += char.lower()

# Check if palindrome using loop
is_palindrome = True
for i in range(len(cleaned) // 2):
    if cleaned[i] != cleaned[-(i + 1)]:
        is_palindrome = False
        break

# Display result
if is_palindrome:
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")
