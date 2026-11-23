from collections import defaultdict


def group_anagrams(words: list[str]) -> list[list[str]]:
    groups = defaultdict(list)

    for word in words:
        key = tuple(sorted(word))
        groups[key].append(word)

    return list(groups.values())