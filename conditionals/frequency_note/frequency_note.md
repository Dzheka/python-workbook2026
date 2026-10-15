# Frequency to Note

Write a program that reverses the process of the previous exercise. Read a frequency from the user and determine if it corresponds to a known musical note.

## Reference Note Frequencies (4th Octave)

| Note | Frequency (Hz) |
|------|----------------|
| C4   | 261.63         |
| D4   | 293.66         |
| E4   | 329.63         |
| F4   | 349.23         |
| G4   | 392.00         |
| A4   | 440.00         |
| B4   | 493.88         |

## Examples

**Example 1:**

```
440
```

```
A4
```

**Example 2:**

```
261
```

```
C4
```

**Example 3:**

```
262.5
```

```
C4
```

**Example 4:**

```
500
```

```
No match
```

**Example 5:**

```
392.8
```

```
G4
```

## Matching Logic

- A frequency matches a note if it's within ±1 Hz of the note's frequency
- For example, A4 (440 Hz) matches frequencies from 439.0 to 441.0
- Check each note systematically to find a match
