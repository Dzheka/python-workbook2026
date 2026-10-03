# Read message and shift amount
message = input()
shift = int(input())

# Initialize result string
result = ""

# Process each character
for char in message:
    if char.isalpha():
        # Determine if uppercase or lowercase
        if char.isupper():
            # Convert to position (A=0, B=1, ..., Z=25)
            pos = ord(char) - ord("A")
            # Apply shift and wrap around
            new_pos = (pos + shift) % 26
            # Convert back to character
            result += chr(new_pos + ord("A"))
        else:
            # Convert to position (a=0, b=1, ..., z=25)
            pos = ord(char) - ord("a")
            # Apply shift and wrap around
            new_pos = (pos + shift) % 26
            # Convert back to character
            result += chr(new_pos + ord("a"))
    else:
        # Non-letter characters remain unchanged
        result += char

# Display result
print(result)
