def marked(card, called):
    called_set = set(called)
    called_set.add(0)

    count = 0
    for row in card:
        for cell in row:
            if cell in called_set:
                count += 1
    return count


def has_bingo(card, called):
    called_set = set(called)
    called_set.add(0)  # free cell is always marked

    n = len(card)
    lines = []

    # add all rows
    for row in card:
        lines.append(row)

    #  add all columns
    for col in range(n):
        lines.append([card[row][col] for row in range(n)])

    # add both diagonals
    lines.append([card[i][i] for i in range(n)])
    lines.append([card[i][n - 1 - i] for i in range(n)])

    for line in lines:
        if set(line) <= called_set:
            return True

    return False