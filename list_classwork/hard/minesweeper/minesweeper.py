def count_mines(field, r, c):
    count = 0

    for dr in range(-1, 2):
        for dc in range(-1, 2):
            if dr == 0 and dc == 0:
                continue

            nr = r + dr
            nc = c + dc

            if 0 <= nr < len(field) and 0 <= nc < len(field[0]):
                if field[nr][nc] == "*":
                    count += 1

    return count


def annotate(field):
    result = []

    for r in range(len(field)):
        row = ""

        for c in range(len(field[0])):
            if field[r][c] == "*":
                row += "*"
            else:
                mines = count_mines(field, r, c)

                if mines == 0:
                    row += "."
                else:
                    row += str(mines)

        result.append(row)

    return result


def safe_squares(field):
    count = 0

    for r in range(len(field)):
        for c in range(len(field[0])):
            if field[r][c] == "." and count_mines(field, r, c) == 0:
                count += 1

    return count