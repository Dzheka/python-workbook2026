def count_coins(amount):
    count = 0
    for coin in (50, 20, 10, 5, 2, 1):
        while amount >= coin:
            amount = amount - coin
            count += 1
    return count

def coin_breakdown(amount):
    