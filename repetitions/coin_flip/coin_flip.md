# Coin Flip Simulation

Simulate coin flips until 3 consecutive identical outcomes occur.

## Task
- Simulate flipping a fair coin repeatedly
- Stop when 3 consecutive heads OR 3 consecutive tails occur
- Display each flip as 'H' or 'T' on one line
- Display the number of flips needed
- Perform 10 simulations
- Report the average number of flips needed

## Example Output
```
H T T T (4 flips)
H H T T H T H T T H H T H T T H T T T (19 flips)
T T T (3 flips)
T H H H (4 flips)
H H H (3 flips)
T H T T H T H H T T H H T H T H H H (18 flips)
H T T H H H (6 flips)
T H T T T (5 flips)
T T H T T H T H T H H H (12 flips)
T H T T T (5 flips)
On average, 7.9 flips were needed.
```

## Logic
1. For 10 simulations:
   - Initialize `consecutive count` = 1
   - Flip coin and store result
   - Display flip
   - Keep flipping until 3 consecutive same outcomes:
     - Generate new flip
     - Display flip
     - If same as previous: increment `consecutive count`
     - If different: reset `consecutive count` to 1
     - Update previous flip
   - Display flip count
2. Calculate and display average
