def get_page(items: list, page_num: int, page_size: int) -> list:
    pages = []
    current_page = []

    for item in items:
        current_page.append(item)

        if len(current_page) == page_size:
            pages.append(current_page)
            current_page = []
    if current_page:
        pages.append(current_page)

    if page_num > len(pages):
        return []

    return pages[page_num - 1]




if __name__ == "__main__":
    # Test your function
    print(get_page(["a", "b", "c", "d", "e"], 1, 2))  # ['a', 'b']
    print(get_page(["a", "b", "c", "d", "e"], 2, 2))  # ['c', 'd']
    print(get_page(["a", "b", "c", "d", "e"], 3, 2))  # ['e']