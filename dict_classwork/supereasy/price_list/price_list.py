def total(prices, basket):
    a = 0

    for i in basket:
        a += prices.get(i, 0)

    return a


def cheapest(prices):
    a = None

    for i in sorted(prices):
        if a is None or prices[i] < prices[a]:
            a = i

    return a