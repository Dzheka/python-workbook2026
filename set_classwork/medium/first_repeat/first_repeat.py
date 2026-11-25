def first_repeat(items):
    item = set()
    for i in items:
        if i in item:
            return i
        item.add(i)


def remove_repeats(items):
    no_repeats = []
    for i in items:
        if i not in no_repeats:
            no_repeats.append(i)
    return no_repeats

print(remove_repeats([3,1,3,2,1]))