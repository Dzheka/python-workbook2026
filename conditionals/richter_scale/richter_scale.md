# Exercise: Richter Scale

Write a program that reads an earthquake magnitude and displays the appropriate descriptor according to the Richter scale.

## Richter Scale Classifications

| Magnitude               | Descriptor |
|-------------------------|------------|
| magnitude < 2.0         | Micro      |
| 2.0 <= magnitude < 3.0  | Very Minor |
| 3.0 <= magnitude < 4.0  | Minor      |
| 4.0 <= magnitude < 5.0  | Light      |
| 5.0 <= magnitude < 6.0  | Moderate   |
| 6.0 <= magnitude < 7.0  | Strong     |
| 7.0 <= magnitude < 8.0  | Major      |
| 8.0 <= magnitude < 10.0 | Great      |
| magnitude >= 10.0       | Meteoric   |

## Examples

**Example 1:**

```
1.5
```

```
Micro
```

**Example 2:**

```
2.5
```

```
Very Minor
```

**Example 3:**

```
5.5
```

```
Moderate
```

**Example 4:**

```
7.2
```

```
Major
```

**Example 5:**

```
8.9
```

```
Great
```

**Example 6:**

```
10.5
```

```
Meteoric
```

## About the Richter Scale

The Richter scale is a **logarithmic scale**, not linear. Each whole number increase represents a 10-fold increase in amplitude and approximately 31.6 times more energy release. For example, a magnitude 5.0 earthquake is 10 times stronger than a magnitude 4.0 earthquake.
