DAY = 24 * 60


def is_valid_time(time):
    if len(time) != 5 or time[2] != ":":
        return False
    for i in (0, 1, 3, 4):
        if time[i] not in "0123456789":
            return False
    hours = int(time[:2])
    minutes = int(time[3:])
    return 0 <= hours <= 23 and 0 <= minutes <= 59


def to_minutes(time):
    return int(time[:2]) * 60 + int(time[3:])


def add_minutes(time, minutes):
    total = (to_minutes(time) + minutes) % DAY
    return f"{total // 60:02d}:{total % 60:02d}"


def duration(start, end):
    return (to_minutes(end) - to_minutes(start)) % DAY


def to_12h(time):
    total = to_minutes(time)
    hours = total // 60
    minutes = total % 60
    suffix = "AM" if hours < 12 else "PM"
    hours12 = hours % 12
    if hours12 == 0:
        hours12 = 12
    return f"{hours12}:{minutes:02d} {suffix}"