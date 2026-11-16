def get_page(items: list, page_num: int, page_size: int) -> list:
    if page_num < 1 or page_size < 1:
        return []
        
    start = (page_num - 1) * page_size
    end = start + page_size
    return items[start:end]
