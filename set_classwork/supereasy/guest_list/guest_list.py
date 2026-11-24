def add_guest(guests, name):
    if name in guests:
        return False
    guests.add(name)
    return True


def remove_guest(guests, name):
    if name not in guests:
        return False
    guests.remove(name)
    return True