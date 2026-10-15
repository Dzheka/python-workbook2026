# Bowling Score (Hard)

A game of ten-pin bowling has **10 frames**. In each frame the player gets
two rolls to knock down 10 pins.

- **Strike** `X`: all 10 pins with the first roll. The frame has one roll
  and scores 10 + the next **two** rolls.
- **Spare** `/`: all 10 pins with two rolls. Scores 10 + the next **one**
  roll.
- Otherwise the frame scores the pins knocked down. A miss is written `-`.

A strike or spare in the 10th frame earns bonus rolls, written at the end.
They only count as bonus, not as frames of their own.

The whole game is one string of rolls:

```
X7/9-X-88/-6XXX81
```

## Task

- Create a function `roll_value(rolls, i)` that returns how many pins roll
  `i` knocked down: `X` is 10, `-` is 0, a digit is itself, and `/` is
  10 minus the roll before it
- Create a function `score(rolls)` that returns the total score of a
  complete game
- Create a function `is_perfect_game(rolls)` that returns `True` for a score
  of 300

## Examples

| Call                                | Returns |
|-------------------------------------|---------|
| `roll_value("7/", 1)`               | `3`     |
| `roll_value("X", 0)`                | `10`    |
| `score("9-9-9-9-9-9-9-9-9-9-")`     | `90`    |
| `score("5/5/5/5/5/5/5/5/5/5/5")`    | `150`   |
| `score("X7/9-X-88/-6XXX81")`        | `167`   |
| `score("XXXXXXXXXXXX")`             | `300`   |
| `is_perfect_game("XXXXXXXXXXX9")`   | `False` |

Hint: walk the string with an index `i` and a `for frame in range(10):`
loop. A strike moves `i` forward by 1, any other frame by 2. Since the loop
stops after 10 frames, the bonus rolls are only ever read as bonus.
