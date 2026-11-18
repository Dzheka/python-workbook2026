def winning(tickets, winners):
    tickets, winners = set(tickets), set(winners)
    return sorted(winners & tickets)

def has_winner(tickets, winners):
    if winning(tickets, winners):
        return True
    return False