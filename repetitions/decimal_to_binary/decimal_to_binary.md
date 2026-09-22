# Decimal to Binary

Convert a decimal (base 10) number to binary (base 2).

## Task
- Read a decimal number from the user as an integer
- Use the division algorithm to convert to binary
- Display the binary representation

## Algorithm
1. Let result be an empty string
2. Let q represent the number to convert
3. Repeat:
   - Set r = remainder when q is divided by 2
   - Convert r to string and add to the BEGINNING of result
   - Divide q by 2 (floor division), store back into q
4. Until q is 0
5. Display result

## Examples
**Example 1:**
```
10
```
```
The binary equivalent is 1010
```

**Example 2:**
```
15
```
```
The binary equivalent is 1111
```

**Example 3:**
```
42
```
```
The binary equivalent is 101010
```

## Logic
- Read decimal number `q`
- Initialize empty result string
- While `q > 0`:
  - `r = q % 2` (remainder)
  - Prepend `r` to result string
  - `q = q // 2` (integer division)
- Display the result
