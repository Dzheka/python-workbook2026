# Progress Bar (Easy)

Draw a text progress bar like the ones in a terminal:

```
[#####-----] 50%
```

## Task

- Create a function `progress_bar(percent, width)` that returns the bar as a
  string:
  - `width` characters between the brackets
  - the number of `#` is `percent * width // 100`; the rest are `-`
  - after the bar: a space, the percent and `%`
  - a percent below 0 is treated as 0, above 100 as 100

## Examples

| Call                      | Returns                         |
|---------------------------|---------------------------------|
| `progress_bar(0, 10)`     | `"[----------] 0%"`             |
| `progress_bar(50, 10)`    | `"[#####-----] 50%"`            |
| `progress_bar(99, 10)`    | `"[#########-] 99%"`            |
| `progress_bar(75, 4)`     | `"[###-] 75%"`                  |
| `progress_bar(120, 10)`   | `"[##########] 100%"`           |
| `progress_bar(-5, 10)`    | `"[----------] 0%"`             |

Hint: `"#" * 3` is `"###"`.
