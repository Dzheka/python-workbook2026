# Group Anagrams - Hint

## Algorithm

- Anagrams become identical when their letters are sorted: "eat", "tea", "ate" all become "aet"
- Use that sorted form as a dictionary key; the value is the list of words sharing it
- Append each word to the list under its sorted form
- The groups are the dictionary's values

## Note

A list of characters is not hashable — join the sorted letters back into a string to use them as a key.
