card = [
    [ 5, 18, 33, 48, 64],
    [12, 21, 31, 52, 70],
    [ 3, 26,  0, 47, 61],
    [ 9, 17, 38, 55, 68],
    [14, 29, 41, 50, 75],
]


def marked(card, called: list):
    counter = 0
    for i in called:
        counter += 1
    return counter

def has_bingo(card, called: list):
    