def fare(km, night):
    total_price = 5.00

    if km <= 10:
        total_price += km * 2.00
    else:
        total_price += 10 * 2.00

        extra_km = km - 10
        total_price += extra_km * 1.50

    if night:
        total_price = total_price * 1.25

    return round(total_price, 2)