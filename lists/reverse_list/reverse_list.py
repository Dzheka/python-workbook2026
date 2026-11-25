def reverse_list(string: str) -> list[int]:
    reverse =  [int(n) for n in string.split()]
    return reverse[::-1]


if __name__ == "__main__":
    # Test your function
    print(reverse_list("2 3 5 7 11"))  # [11, 7, 5, 3, 2]
    print(reverse_list("10 -5 3"))     # [3, -5, 10]
    print(reverse_list(""))           # []
