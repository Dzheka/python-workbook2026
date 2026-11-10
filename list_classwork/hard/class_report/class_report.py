def letter(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def ranking(records):
    ordered = sorted(records, key=lambda r: (-r[1], r[0]))
    return [name for name, score in ordered]


def report(records):
    ordered = sorted(records, key=lambda r: (-r[1], r[0]))
    lines = []
    previous_score = None
    place = 0

    for index, (name, score) in enumerate(ordered, start=1):
        if score != previous_score:
            place = index
            previous_score = score

        grade = letter(score)
        lines.append(f"{place}. {name} - {score} ({grade})")

    return "\n".join(lines)


def failed(records):
    result = []

    for name, score in records:
        if letter(score) == "F":
            result.append(name)

    return result