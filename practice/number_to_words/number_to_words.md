# Number to Words (Very Hard)

Write a program that reads an integer from −999 999 999 to 999 999 999 and
prints it in English words.

## Rules

- All words are lowercase and separated by single spaces
- Tens and ones are joined with a hyphen: `twenty-one`, `ninety-nine`
- No word "and": `one hundred five`, not "one hundred and five"
- Parts that are zero are skipped: `1000` is `one thousand`
- `0` is `zero`; a negative number starts with `minus`

## Task

- Write a function `below_100(n)` that turns a number from 0 to 99 into words
- Write a function `below_1000(n)` that turns a number from 0 to 999 into
  words, using `below_100`
- Write a function `number_to_words(n)` that turns any number in the range
  into words, using `below_1000` for the millions, the thousands and the rest
- Read the number and print its words

## Examples

**Example 1:**

```
2024
```

```
two thousand twenty-four
```

**Example 2:**

```
100001
```

```
one hundred thousand one
```

**Example 3:**

```
-90
```

```
minus ninety
```

**Example 4:**

```
123456789
```

```
one hundred twenty-three million four hundred fifty-six thousand seven hundred eighty-nine
```
