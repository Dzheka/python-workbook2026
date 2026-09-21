# Is a String a Palindrome?

Determine whether a string is a palindrome (identical forward and backward).

## Task
- Read a string from the user
- Use a loop to check if it's a palindrome
- Display whether it is or isn't a palindrome

## Examples of Palindromes
- "anna"
- "civic"
- "level"
- "hannah"
- "racecar"

## Examples
**Example 1:**
```
anna
```
```
`anna` is a palindrome
```

**Example 2:**
```
hello
```
```
`hello` is not a palindrome
```

**Example 3:**
```
racecar
```
```
`racecar` is a palindrome
```

## Logic
- Compare first character with last, second with second-to-last, etc.
- Use a loop to iterate through half the string
- If any pair doesn't match, it's not a palindrome
- For index `i`, compare `string[i]` with `string[-(i+1)]`

## Fun Facts
- Aibohphobia: fear of palindromes (itself a palindrome!)
- Ailihphilia: love of palindromes
