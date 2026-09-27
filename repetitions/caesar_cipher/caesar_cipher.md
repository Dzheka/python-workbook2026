# Caesar Cipher

Implement a Caesar cipher to encode/decode messages by shifting letters.

## Task
- Read a message from the user
- Read a shift amount from the user
- Shift each letter by the specified amount
- Display the encoded/decoded message
- Support both uppercase and lowercase letters
- Support negative shift values (for decoding)
- Non-letter characters remain unchanged

## Examples
**Example 1:**
```
HELLO
3
```
```
KHOOR
```

**Example 2:**
```
xyz
3
```
```
abc
```

**Example 3:**
```
Hello, World!
-3
```
```
Ebiil, Tloia!
```

## Logic
- For each character in the message:
  - If it's a letter:
    - Convert to position (A=0, B=1, ..., Z=25)
    - Add `shift` value
    - Use modulo 26 to wrap around
    - Convert back to letter
  - If not a letter, keep it unchanged
- Maintain case (uppercase stays uppercase, lowercase stays lowercase)
