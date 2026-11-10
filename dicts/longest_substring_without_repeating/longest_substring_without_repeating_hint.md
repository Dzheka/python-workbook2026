# Longest Substring Without Repeating Characters - Hint

## Algorithm

- Slide a window over the string: `left` marks the window start, `right` scans forward one character at a time
- Keep a dictionary mapping each character to the index where it was last seen
- If the current character was last seen inside the window, move `left` to just past that previous occurrence
- Record the character's new position and track the largest window size seen

## Note

Each character enters and leaves the window at most once, making this O(n) instead of checking every substring.
