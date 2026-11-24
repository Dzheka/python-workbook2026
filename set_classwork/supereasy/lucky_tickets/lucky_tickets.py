def winning(tickets, winners):
    res = []
    for i in tickets:
        if i in winners:
           res.append(i)
    return sorted(set(res))

def has_winner(tickets, winners):
    if winning(tickets, winners):
        return True
    return False
