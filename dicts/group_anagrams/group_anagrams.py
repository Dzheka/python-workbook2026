# grid = [[0] * 3 for _ in range(3)]
# grid[0][0] = 1
# grid[1][0] = 1
#grid[2][0] = 1
#print(grid)
def group_anagrams(words: list[str]) -> list[list[str]]:
    groups = {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
