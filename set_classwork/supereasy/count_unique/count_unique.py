def count_unique(items):
    return len(set(items))

def all_different(items):
    return sorted(items) == sorted(set(items))
