def add_guest(guests, name):
    if name not in guests:
        guests.add(name)
        return True
    else:
        return False


def remove_guest(guests, name):
    if name in guests:
        guests.remove(name)
        return True
    else:
        return False