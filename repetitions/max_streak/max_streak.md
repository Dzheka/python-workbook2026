# Maximum Streak

Game results arrive one per line — `1` for a win, `0` for a loss — ending with
a blank line. A streak is a run of consecutive wins, and any loss breaks it.
Read the results and display the length of the longest winning streak.

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
