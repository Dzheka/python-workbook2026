def fare(km, night):
    if km <= 10:
        price = 5 + km * 2
    else:
        price = 5 + 10 * 2 + (km - 10) * 1.5

    if night:
        price *= 1.25

    return price
