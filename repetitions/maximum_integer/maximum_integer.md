# Maximum Integer

Simulate finding the maximum value in a collection of 100 random integers.

## Task
- Generate 100 random integers between 1 and 100
- Track the maximum value encountered
- Count how many times the maximum was updated
- Display each integer, marking new maximums
- Display final statistics

## Example Output
```
30
74 <== Update
58
17
40
37
13
34
46
52
80 <== Update
37
97 <== Update
45
55
73
...
The maximum value found was 100
The maximum value was updated 5 times
```

## Logic
1. Generate first random integer as initial maximum
2. Set update count to 0
3. For the next 99 integers:
   - Generate random integer
   - Display it
   - If it's larger than current maximum:
     - Update maximum
     - Increment update count
     - Display " <== Update" on same line
4. Display final maximum and update count
