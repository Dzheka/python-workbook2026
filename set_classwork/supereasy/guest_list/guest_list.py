def add_guest(guests: set, name: str) -> bool:
    if name not in guests:
        guests.add(name)
        return True
    return False

def remove_guest(guests: set, name: str) -> bool:
    if name in guests:
        guests.remove(name)
        return True
    return False
