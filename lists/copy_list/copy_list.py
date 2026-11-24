def copy_list(l: list) -> list:
    temp = []
    for i in l:
        temp.append(i)
    return temp


def are_different_objects(l1: list, l2: list) -> bool:
    return l1 is not l2


if __name__ == "__main__":
    # Test your functions
    original = [2, 3, 5, 7, 11]
    copied = copy_list(original)
    print(copied)  # [2, 3, 5, 7, 11]
    print(are_different_objects(original, copied))  # True