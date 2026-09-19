# Exercise: Frequency to Name

Write a program that classifies electromagnetic radiation based on its frequency.

## Electromagnetic Radiation Classifications

| Name              | Frequency Range (Hz)                   |
|-------------------|----------------------------------------|
| Radio Waves       | Less than `3 × 10⁹`                    |
| Microwaves        | `3 × 10⁹` to less than `3 × 10¹²`      |
| Infrared Light    | `3 × 10¹²` to less than `4.3 × 10¹⁴`   |
| Visible Light     | `4.3 × 10¹⁴` to less than `7.5 × 10¹⁴` |
| Ultraviolet Light | `7.5 × 10¹⁴` to less than `3 × 10¹⁷`   |
| X-Rays            | `3 × 10¹⁷` to less than `3 × 10¹⁹`     |
| Gamma Rays        | `3 × 10¹⁹` or more                     |

## Examples

**Example 1:**

```
1000000000
```

```
Radio Waves
```

**Example 2:**

```
10000000000
```

```
Microwaves
```

**Example 3:**

```
500000000000000
```

```
Visible Light
```

**Example 4:**

```
1000000000000000000
```

```
Ultraviolet Light
```

**Example 5:**

```
100000000000000000000
```

```
Gamma Rays
```
