def reverse_list(string: str) -> list[int]:
    string = string.split()
    rev = []
    for i in string[::-1]:
        rev.append(int(i))
    return  rev


if __name__ == "__main__":
    # Test your function
    print(reverse_list("2 3 5 7 11"))  # [11, 7, 5, 3, 2]
    print(reverse_list("10 -5 3"))     # [3, -5, 10]
    print(reverse_list(""))           # []