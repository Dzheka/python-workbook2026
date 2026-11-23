def total(prices):
    result = 0
    for price in prices:
        result += price
    return result


def can_afford(prices, money):
    if money >= total(prices):
        return "yes"
    return "no"