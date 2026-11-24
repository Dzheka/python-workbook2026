def longest_substring_without_repeating(s: str) -> int:
    max_len = 0
    d = ""

    for ch in s:
        if ch in d:
            dup_idx = d.index(ch)
            d = d[dup_idx + 1:]

        d += ch
        if max_len < len(d):
            max_len = len(d)

    return max_len





if __name__ == "__main__":
    print(longest_substring_without_repeating("abcabcbb"))  # 3 ("abc")
    print(longest_substring_without_repeating("bbbbb"))  # 1 ("b")
    print(longest_substring_without_repeating("pwwkew"))  # 3 ("wke")
    print(longest_substring_without_repeating(""))  # 0
    print(longest_substring_without_repeating("a"))  # 1
    print(longest_substring_without_repeating("abcdef"))  # 6
    print(longest_substring_without_repeating("dvdf"))  # 3 ("vdf")