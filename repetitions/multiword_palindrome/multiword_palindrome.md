# Multiple Word Palindromes

Determine if a phrase is a palindrome when spacing (and optionally punctuation) is ignored.

## Task
- Read a string from the user
- Check if it's a palindrome ignoring spaces
- **Optional Challenge:** Also ignore punctuation and treat uppercase/lowercase as equivalent
- Display whether it is or isn't a palindrome

## Examples of Multi-word Palindromes
- "go dog"
- "flee to me remote elf"
- "some men interpret nine memos"
- "A man a plan a canal Panama" (with case/punctuation ignored)

## Examples
**Example 1:**
```
`go dog`
```
```
`go dog` is a palindrome
```

**Example 2:**
```
`flee to me remote elf`
```
```
`flee to me remote elf` is a palindrome
```

**Example 3:**
```
`hello world`
```
```
`hello world` is not a palindrome
```

## Logic
- Remove spaces from the string
- Convert to same case (for advanced version)
- Remove punctuation (for advanced version)
- Check if modified string is a palindrome
{{ ... }}
- If any pair doesn't match, it's not a palindrome
- For index `i`, compare `cleaned[i]` with `cleaned[-(i+1)]`
