# Fizz Buzz

Write a program that implements the FizzBuzz logic for a single number.

## FizzBuzz Rules

- If divisible by `3` only: "Fizz"
- If divisible by `5` only: "Buzz"
- If divisible by both `3` and `5`: "FizzBuzz"
- Otherwise: display the number itself

## Examples

**Example 1:**

```
15
```

```
FizzBuzz
```

**Example 2:**

```
9
```

```
Fizz
```

**Example 3:**

```
10
```

```
Buzz
```

**Example 4:**

```
7
```

```
7
```

**Example 5:**

```
30
```

```
FizzBuzz
```

**Example 6:**

```
1
```

```
1
```

## Logic Order (Important)

1. Check if divisible by both `3` AND `5` first
2. Then check if divisible by `3` only
3. Then check if divisible by `5` only
4. Otherwise, return the number

## Note

- Use modulus operator (`%`) to check divisibility
- Check the combined condition (`3` AND `5`) first
- Classic programming interview question
