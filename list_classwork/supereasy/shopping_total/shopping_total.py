def total(prices):
    return sum(prices)

def can_afford(prices, money):
    return 'yes' if sum(prices) <= money else 'no'