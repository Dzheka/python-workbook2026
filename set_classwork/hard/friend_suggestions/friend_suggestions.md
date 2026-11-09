# Friend Suggestions (Hard)

A social network stores friendships as pairs. Friendship works both ways:
`["Ali", "Sara"]` means Ali is Sara's friend **and** Sara is Ali's.

```python
pairs = [
    ["Ali", "Sara"], ["Ali", "Bek"], ["Sara", "Nilu"],
    ["Bek", "Nilu"], ["Bek", "Timur"], ["Nilu", "Madina"],
]
```

The network suggests new friends: people who are friends of your friends, but
not you and not already your friend. The more friends you share with someone
(*mutual friends*), the higher they are on the list.

## Task

- Create a function `friends_of(pairs, name)` that returns the friends of
  `name`, sorted alphabetically
- Create a function `suggestions(pairs, name)` that returns the suggested
  people, ordered by number of mutual friends (most first); people with the
  same number are ordered alphabetically

A person with no friends, or a name not in the network, has no friends and no
suggestions.

## Examples

| Call                           | Returns                    |
|--------------------------------|----------------------------|
| `friends_of(pairs, "Ali")`     | `["Bek", "Sara"]`          |
| `friends_of(pairs, "Zara")`    | `[]`                       |
| `suggestions(pairs, "Ali")`    | `["Nilu", "Timur"]`        |
| `suggestions(pairs, "Nilu")`   | `["Ali", "Timur"]`         |

Ali's friends are Bek and Sara. Nilu is a friend of **both** of them (2 mutual
friends), Timur only of Bek (1), so Nilu comes first.

Hint: write a helper that returns a **set** of friends; `friends_of` just
sorts it. Collect friends of friends with `|=`, then remove your own friends
and yourself. The number of mutual friends of a person `p` is
`len(friends(p) & my_friends)` — use it in `sorted(..., key=lambda p: ...)`.
