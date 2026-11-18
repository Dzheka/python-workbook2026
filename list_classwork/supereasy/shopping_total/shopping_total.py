def total(prices: list[int]) -> int:
    result = 0
    for price in prices:
        result += price
    return result


def can_afford(prices: list[int], money: int) -> str:
    if money >= total(prices):
        return "yes"
    return "no"
