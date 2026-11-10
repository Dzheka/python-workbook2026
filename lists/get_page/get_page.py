def get_page(items: list, page_num: int, page_size: int):
    a = (page_num - 1) * page_size
    b = a + page_size
    return items[a:b]