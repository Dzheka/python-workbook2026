# Read string from user
string = input()

# Check if palindrome using loop
is_palindrome = True
for i in range(len(string) // 2):
    if string[i] != string[-(i + 1)]:
        is_palindrome = False
        break

# Display result
if is_palindrome:
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")
