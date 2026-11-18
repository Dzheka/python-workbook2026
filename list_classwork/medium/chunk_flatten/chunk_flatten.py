def chunk(items, size):
    pages = []
    current_page = []

    for item in items:
        current_page.append(item)

        if len(current_page) == size:
            pages.append(current_page)
            current_page = []
    if current_page:
        pages.append(current_page)

    return pages


def flatten(nested):
    total_list = []
    for i in nested:
        for j in i:
            total_list.append(j)
    return total_list

def interleave(a, b):
    result = []

    for i in range(max(len(a), len(b))):
        if i < len(a):
            result.append(a[i])
        if i < len(b):
            result.append(b[i])

    return result





