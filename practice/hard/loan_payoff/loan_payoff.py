def monthly_interest(b, y_r):
    return b * y_r / 100 / 12

def months_to_repay(l, y_r, p):
    if monthly_interest(l, y_r) >= p:
        return -1
    b = l
    m = 0
    while b > 0:
        i = monthly_interest(b, y_r)
        b += i
        if b < p:
            b = 0
        else:
            b -= p
        m += 1
    return m


def total_paid(l, y_r, p):
    if monthly_interest(l, y_r) >= p:
        return -1
    b = l
    t = 0.0
    while b > 0:
        i = monthly_interest(b, y_r)
        b += i
        if b < p:
            t += b 
            b = 0
        else:
            b -= p
            t += p
            
    return round(t, 2)

