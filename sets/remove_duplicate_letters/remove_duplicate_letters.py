def remove_duplicate_letters(text: str) -> str:
    ans = ""
    for i in text:
        if i not in ans:
            ans += i
    return ans

if __name__ == "__main__":
    print(remove_duplicate_letters("hello"))  # "helo"
    print(remove_duplicate_letters("mississippi"))  # "misp"
    print(remove_duplicate_letters("abcabc"))  # "abc"
    print(remove_duplicate_letters("AaAaBb"))  # "AaBb"
    print(remove_duplicate_letters(""))  # ""
