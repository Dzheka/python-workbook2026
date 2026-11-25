# Group Words (Medium)

Put words into groups. The result is a dictionary: group → list of words in
that group.

## Task

- Create a function `by_length(words)` that groups the words by their length
- Create a function `by_first_letter(words)` that groups the words by their
  first letter, in lowercase (`"Apple"` and `"avocado"` go to group `"a"`)

Inside every group, keep the words in the order they appear in `words`.
Every word has at least one letter.

## Examples

| Call                                            | Returns                                    |
|-------------------------------------------------|--------------------------------------------|
| `by_length(["hi", "cat", "yo", "dog"])`         | `{2: ["hi", "yo"], 3: ["cat", "dog"]}`     |
| `by_length([])`                                 | `{}`                                       |
| `by_first_letter(["Apple", "bus", "avocado"])`  | `{"a": ["Apple", "avocado"], "b": ["bus"]}`|

Hint: `groups.setdefault(key, []).append(word)` creates the list the first
time a key is seen.
