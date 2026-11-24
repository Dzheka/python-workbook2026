def lookup(book, name):
    return book.get(name, "not found")


def names(book):
    return sorted(book)


def has_number(book, number):
    return number in book.values()