# Pascal's Triangle (Hard)

Every number in Pascal's triangle is the sum of the two above it:

```
      1
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1
1 5 10 10 5 1
```

Row `n` (counting from 0) is made of the binomial coefficients
`C(n, 0), C(n, 1), ..., C(n, n)`, where

```
C(n, k) = n · (n-1) · ... · (n-k+1) / (1 · 2 · ... · k)
```

Do not use `math.comb` — compute it with a loop.

## Task

- Create a function `binomial(n, k)` that returns `C(n, k)`, or `0` if `k`
  is below 0 or above `n`
- Create a function `pascal_row(n)` that returns row `n` as numbers
  separated by single spaces
- Create a function `pascal_triangle(rows)` that returns the first `rows`
  rows as one string joined by `"\n"`. Each row is moved right by
  `(width - len(row)) // 2` spaces, where `width` is the length of the last
  row. No spaces at the end of lines.

## Examples

| Call                     | Returns                                 |
|--------------------------|-----------------------------------------|
| `binomial(4, 2)`         | `6`                                     |
| `binomial(10, 3)`        | `120`                                   |
| `binomial(5, 6)`         | `0`                                     |
| `pascal_row(0)`          | `"1"`                                   |
| `pascal_row(4)`          | `"1 4 6 4 1"`                           |
| `pascal_row(10)`         | `"1 10 45 120 210 252 210 120 45 10 1"` |
| `pascal_triangle(3)`     | `"  1\n 1 1\n1 2 1"`                    |

Hint: to stay with whole numbers, update the result one step at a time:
`result = result * (n - i + 1) // i` for `i` from 1 to `k`. The division is
always exact.
