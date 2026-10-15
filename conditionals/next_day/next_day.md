# Exercise: Next Day

Write a program that reads a date and computes its immediate successor (next day).

## Examples

**Example 1:** (Regular day)

```
2019
11
18
```

```
2019-11-19
```

**Example 2:** (End of month)

```
2019
11
30
```

```
2019-12-01
```

**Example 3:** (End of year)

```
2019
12
31
```

```
2020-01-01
```

**Example 4:** (Leap year)

```
2020
2
28
```

```
2020-02-29
```

**Example 5:** (Non-leap year)

```
2021
2
28
```

```
2021-03-01
```

## Days in Each Month

| Month                 | Days     | Notes                |
|-----------------------|----------|----------------------|
| 1, 3, 5, 7, 8, 10, 12 | 31       |                      |
| 4, 6, 9, 11           | 30       |                      |
| 2                     | 28 or 29 | Depends on leap year |
