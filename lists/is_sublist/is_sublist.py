def is_sublist(main_list: list, sub: list) -> bool:

    for i in range(len(main_list) - len(sub) + 1):
        if main_list[i:i + len(sub)] == sub:
            return True

    return False
if __name__ == "__main__":
    print(is_sublist([2, 3, 5, 7, 11], [3, 5, 7]))  # True
    print(is_sublist([2, 3, 5, 7, 11], [3, 7]))  # False
    print(is_sublist([2, 3, 5], []))  # True