def winning(tickets, winners):
    return sorted(set(tickets) & set(winners))


def has_winner(tickets, winners):
    return not set(tickets).isdisjoint(winners)