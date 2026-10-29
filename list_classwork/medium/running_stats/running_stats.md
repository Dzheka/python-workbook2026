# Running Stats (Medium)

A shop writes down how much it earned each day. The owner wants to see how the
numbers move over time.

## Task

- Create a function `running_sum(nums)` that returns a new list where item
  `i` is the sum of all numbers up to and including `nums[i]`
- Create a function `longest_growth(nums)` that returns the length of the
  longest stretch of days where every day earned **more** than the day
  before (one day on its own is a stretch of length `1`; an empty list
  gives `0`)
- Create a function `best_window(nums, k)` that returns the largest sum of
  `k` days **in a row**; if there are fewer than `k` days, return `0`

## Examples

| Call                                        | Returns            |
|---------------------------------------------|--------------------|
| `running_sum([3, 1, 4, 1])`                 | `[3, 4, 8, 9]`     |
| `running_sum([])`                           | `[]`               |
| `longest_growth([1, 2, 3, 1, 5, 6, 7, 8])`  | `5`                |
| `longest_growth([5, 5, 5])`                 | `1`                |
| `best_window([1, 9, 2, 8, 3], 2)`           | `11`               |
| `best_window([4, -1, 2], 3)`                | `5`                |
| `best_window([1, 2], 3)`                    | `0`                |

Hint: for `longest_growth`, keep two counters: the current stretch and the
best one seen so far. `sum(nums[i:i + k])` is the sum of one window.
