# Parity Bits

Compute the parity bit for groups of 8 bits using even parity.

## Task
- Read strings of 8 bits from the user
- Continue until blank line is entered
- For each string, compute the parity bit using even parity
- Display whether parity bit should be 0 or 1
- Display error if input is not exactly 8 bits

## Even Parity
- Count the number of 1s in the 8-bit string
- If count is even: parity bit = 0
- If count is odd: parity bit = 1
- Goal: total 1s (including parity bit) is even

## Examples
**Example 1:** (several strings, then a blank line to stop)
```
00000000
10101010
10101011

```
```
Parity bit: 0
Parity bit: 0
Parity bit: 1
```

**Example 2:** (input that isn't 8 bits)
```
1010

```
```
Error: Input must be exactly 8 bits
```
