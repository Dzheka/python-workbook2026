# H2O Phases

Write a program that determines the phase of water based on temperature.

## Temperature Ranges

| Temperature (°C) | Phase           |
|------------------|-----------------|
| Below 0          | solid           |
| 0 to 100         | liquid          |
| Above 100        | gas             |

## Examples

**Example 1:**

```
-10
```

```
solid
```

**Example 2:**

```
25
```

```
liquid
```

**Example 3:**

```
0
```

```
solid or liquid
```

## Notes

- At exactly 0°C, water can be either solid or liquid (display "solid or liquid")
- At exactly 100°C, water can be either liquid or gas (display "liquid or gas")
- Consider standard atmospheric pressure (1 atm)
