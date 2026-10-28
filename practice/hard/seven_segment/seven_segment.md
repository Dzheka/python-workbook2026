# Seven-Segment Display (Hard)

Draw numbers the way a digital clock does, 3 characters wide and 3 lines
tall:

```
 _     _  _     _  _  _  _  _ 
| |  | _| _||_||_ |_   ||_||_|
|_|  ||_  _|  | _||_|  ||_| _|
```

That is 0 1 2 3 4 5 6 7 8 9. Copy these three lines into your code as three
strings — digit `d` takes characters `3·d` to `3·d + 2` of each line.

## Task

- Create a function `digit_row(digit, row)` that returns the 3 characters
  of `digit` in line `row` (0 top, 1 middle, 2 bottom)
- Create a function `render(number)` that returns the whole number as one
  string of 3 lines joined by `"\n"`: the digits side by side, no gaps
  between them, nothing removed from the ends of the lines
- Create a function `segment_count(number)` that returns how many segments
  (characters that are not spaces) the display lights up for `number`

## Examples

| Call                  | Returns                 |
|-----------------------|-------------------------|
| `digit_row(0, 1)`     | `"\| \|"`               |
| `digit_row(9, 2)`     | `" _\|"`                |
| `render(8)`           | `" _ \n\|_\|\n\|_\|"`   |
| `segment_count(8)`    | `7`                     |
| `segment_count(1)`    | `2`                     |
| `segment_count(2026)` | `22`                    |

`print(render(2026))` shows:

```
 _  _  _  _ 
 _|| | _||_ 
|_ |_||_ |_|
```

Hint: build the result line by line — the outer loop goes over the 3 rows,
the inner loop over the digits of `str(number)`.
