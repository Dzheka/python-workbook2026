def total(prices):
    a = 0

    for i in prices:
        a += i

    return a


def can_afford(prices, money):
    if money >= total(prices):
        return "yes"
    else:
        return "no"