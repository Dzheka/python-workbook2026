def is_sublist(main_list: list, sub: list):
    for i in range(len(main_list) - len(sub) + 1):
        if main_list[i:i + len(sub)] == sub:
            return True

    return False
