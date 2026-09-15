# Exercise: Vowel or Consonant

Create a program that reads a letter of the alphabet from the user and determines whether it is a vowel, consonant, or the special case of `'y'`.

## Examples

**Example 1:**

```
a
```

```
vowel
```

**Example 2:**

```
b
```

```
consonant
```

**Example 3:**

```
y
```

```
sometimes vowel, sometimes consonant
```

**Example 4:**

```
A
```

```
vowel
```

## Logic

- If letter is `'y'`: display "sometimes vowel, sometimes consonant"
- If letter is `'a'`, `'e'`, `'i'`, `'o'`, `'u'` (case-insensitive): display "vowel"
- If the letter is any other alphabetic character: display "consonant"

## Note

- Handle both uppercase and lowercase letters
- The letter 'y' is a special case in English - it can function as either a vowel or consonant depending on context
- Vowels are: a, e, i, o, u
- All other letters of the alphabet are consonants
