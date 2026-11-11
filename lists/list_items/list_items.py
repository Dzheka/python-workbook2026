def first_item(items):
    return items[0]


def mid_item(items):
    return  items[len(items) // 2]


def last_item(items):
    return items[-1]


if __name__ == "__main__":
    # Test your functions
    items = [2, 3, 5, 7, 11]
    print(first_item(items))  # 2
    print(mid_item(items))    # 5
    print(last_item(items))   # 11-