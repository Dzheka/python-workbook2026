# The Collatz Conjecture

Generate and display Collatz sequences for integers entered by the user.

## Task
- Read an integer `n` from the user
- Display the Collatz sequence starting with `n` and ending with 1
- Continue reading new values until user enters `n` ≤ 0

## The Collatz Sequence Algorithm
1. Start with any positive integer `n`
2. While `n` is not equal to 1:
   - If `n` is even: divide by 2 (floor division)
   - If `n` is odd: multiply by 3 and add 1
3. The sequence ends when `n` reaches 1

## Examples
**Example 1:**
```
5
```
```
5 16 8 4 2 1
```

**Example 2:**
```
10
```
```
10 5 16 8 4 2 1
```

**Example 3:**
```
1
```
```
1
```

## Logic
- Use a while loop to read integers from user
- For each `n` > 0:
  - Display `n`
  - While `n` != 1:
    - If `n` is even: `n` = `n` // 2
    - If `n` is odd: `n` = `n` * 3 + 1
    - Display `n`
  - Read next number
- Stop when user enters `n` ≤ 0
