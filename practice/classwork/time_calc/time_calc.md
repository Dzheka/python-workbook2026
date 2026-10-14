# Clock Arithmetic (Hard)

Times are written as strings `"HH:MM"` on a 24-hour clock: always two digits
for the hours, a colon, two digits for the minutes. After `"23:59"` comes
`"00:00"` again.

## Task

- Create a function `is_valid_time(time)` that returns `True` if `time` is
  exactly 5 characters long, has `:` in the middle, digits around it, hours
  from 0 to 23 and minutes from 0 to 59
- Create a function `to_minutes(time)` that returns how many minutes have
  passed since midnight
- Create a function `add_minutes(time, minutes)` that returns the time
  `minutes` later, in the same `"HH:MM"` format; `minutes` may be negative and
  may be larger than a whole day
- Create a function `duration(start, end)` that returns how many minutes pass
  from `start` to the *next* `end`; if `end` is earlier than `start`, the
  interval goes through midnight
- Create a function `to_12h(time)` that converts the time to the 12-hour
  format: `"9:30 AM"`, `"1:05 PM"` — no leading zero in the hours; midnight
  hour is `12 ... AM`, noon hour is `12 ... PM`

Reuse `to_minutes` inside the other functions. All functions except
`is_valid_time` may assume that their input is valid.

## Examples

| Call                              | Returns      |
|-----------------------------------|--------------|
| `is_valid_time("23:59")`          | `True`       |
| `is_valid_time("24:00")`          | `False`      |
| `is_valid_time("7:30")`           | `False`      |
| `to_minutes("13:45")`             | `825`        |
| `add_minutes("23:45", 30)`        | `"00:15"`    |
| `add_minutes("00:10", -20)`       | `"23:50"`    |
| `add_minutes("08:15", 3000)`      | `"10:15"`    |
| `duration("09:00", "17:30")`      | `510`        |
| `duration("23:30", "01:15")`      | `105`        |
| `to_12h("00:15")`                 | `"12:15 AM"` |
| `to_12h("12:00")`                 | `"12:00 PM"` |
| `to_12h("13:05")`                 | `"1:05 PM"`  |

Hint: `%` with `24 * 60` wraps any number of minutes into one day — even a
negative one.
