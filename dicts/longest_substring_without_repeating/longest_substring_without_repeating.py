def longest_substring_without_repeating(s):
    seen = {}
    left = ans = 0

    for right, char in enumerate(s):
        if char in seen:
            left = max(left, seen[char] + 1)

        seen[char] = right
        ans = max(ans, right - left + 1)

    return ans

