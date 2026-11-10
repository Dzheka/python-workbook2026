# Two Sum - Hint

## Algorithm

- Walk the list once, remembering each number's index in a dictionary as you go
- For each number, compute its complement: the value that would add up to the target
- If the complement is already in the dictionary, return its stored index and the current index
- Otherwise store the current number with its index and continue

## Note

Checking the dictionary before storing the current number guarantees the same element is never used twice, and one pass is O(n) instead of the O(n²) nested-loop search.
