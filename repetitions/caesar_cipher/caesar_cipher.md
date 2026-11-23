# Caesar Cipher

Julius Caesar protected his military orders with a simple trick: shift every
letter a fixed number of places along the alphabet. With a shift of 3, `A`
becomes `D`, `B` becomes `E`, and `Z` wraps back around to `C`. To read the
message, you shift the other way.

## Task
- Read a message, then a shift amount
- Shift each letter by that amount, wrapping around the alphabet
- Keep each letter's case; leave non-letter characters unchanged
- A negative shift decodes a message

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
KHOOR
-3
```
```
HELLO
```

**Example 3:**
```
xyz
3
```
```
abc
```

**Example 4:**
```
Hello, World!
3
```
```
Khoor, Zruog!
```
