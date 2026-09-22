# Maximum Streak

Find the longest winning streak in a series of game results.

## Task
- Read game results from the user until a blank line is entered
- Each result is either `1` (win/success) or `0` (loss/failure)
- A streak is consecutive wins (1s)
- Any loss (0) breaks the current streak
- Display the maximum winning streak length

## Examples
**Example 1:**
```
1
1
1
0
1
1

```
```
Maximum streak: 3
```
*Explanation: First 3 wins, then a loss breaks it, then 2 wins. Max = 3*

**Example 2:**
```
1
1
1
1
1

```
```
Maximum streak: 5
```
*Explanation: 5 consecutive wins*

**Example 3:**
```
0
1
0
1
1
1
0

```
```
Maximum streak: 3
```
*Explanation: Loss, win, loss, then 3 wins. Max = 3*

**Example 4:**
```
0
0
0

```
```
Maximum streak: 0
```
*Explanation: All losses, no winning streak*

## Logic
- Track current streak of consecutive wins (1s)
- Track maximum streak seen so far
- As you read each value:
  - If it's a win (1): increment current streak
  - If it's a loss (0): compare current streak to max, then reset current streak to 0
- After loop ends, compare final streak to max (in case the input ends on a winning streak)
