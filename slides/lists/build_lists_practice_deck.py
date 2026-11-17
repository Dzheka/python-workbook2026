"""Build the "Race" deck — list practice solved live, first correct wins.

Ten tasks on one topic each, easiest first, every one a single slide: the task,
a worked example, and the input the class must run it on. Answers live in the
second half of the deck, so the teacher can reveal them one at a time.

The scoring is on the rules slide: the first correct answer takes the point.

Every expected answer on these slides was produced by running the code.

Run:  uv run --with python-pptx python slides/lists/build_lists_practice_deck.py
"""

from pathlib import Path

from _deck import (
    BODY_TOP,
    GRAY,
    M,
    NAVY,
    W,
    H,
    WHITE,
    YELLOW,
    RGBColor,
    Inches,
    _box,
    _para,
    _tf,
    bullets,
    code,
    note,
    out,
    prs,
    save,
    section,
    slide,
    table,
)

OUT = Path(__file__).with_name("lists_practice.pptx")

# Each task: number, title, what to write, the example, the input to run on,
# the expected answer, and the model solution shown later.
TASKS = [
    {
        "n": 1,
        "title": "Second largest",
        "ask": "Print the second largest number in the list. Equal numbers "
        "count once: in [4, 9, 2, 9, 7] the largest is 9 and the "
        "second largest is 7.",
        "data": "numbers = [4, 9, 2, 9, 7]",
        "answer": "7",
        "solution": [
            "numbers = [4, 9, 2, 9, 7]",
            "",
            "unique = sorted(set(numbers))",
            "print(unique[-2])",
        ],
        "note": "`set` throws the duplicates away, `sorted` puts them in "
        "order, `[-2]` takes the one before last.",
    },
    {
        "n": 2,
        "title": "Drop the duplicates",
        "ask": "Build a new list with every number kept once, in the order "
        "they first appeared.",
        "data": "numbers = [4, 9, 2, 9, 7, 4]",
        "answer": "[4, 9, 2, 7]",
        "solution": [
            "numbers = [4, 9, 2, 9, 7, 4]",
            "seen = []",
            "",
            "for n in numbers:",
            "    if n not in seen:",
            "        seen.append(n)",
            "",
            "print(seen)",
        ],
        "note": "`set(numbers)` also removes duplicates but loses the order — "
        "that is why the loop is worth writing.",
    },
    {
        "n": 3,
        "title": "Running totals",
        "ask": "Print a list where each item is the total of everything up to "
        "and including that position.",
        "data": "numbers = [3, 1, 4, 1, 5]",
        "answer": "[3, 4, 8, 9, 14]",
        "solution": [
            "numbers = [3, 1, 4, 1, 5]",
            "totals = []",
            "running = 0",
            "",
            "for n in numbers:",
            "    running = running + n",
            "    totals.append(running)",
            "",
            "print(totals)",
        ],
        "note": "One accumulator plus one list. The accumulator is created "
        "*before* the loop — inside it, and it resets every turn.",
    },
    {
        "n": 4,
        "title": "Flatten it",
        "ask": "Turn a list of lists into one flat list.",
        "data": "rows = [[1, 2], [3], [4, 5, 6]]",
        "answer": "[1, 2, 3, 4, 5, 6]",
        "solution": [
            "rows = [[1, 2], [3], [4, 5, 6]]",
            "flat = []",
            "",
            "for row in rows:",
            "    for item in row:",
            "        flat.append(item)",
            "",
            "print(flat)",
        ],
        "note": "A loop inside a loop: the outer one walks the rows, the "
        "inner one walks that row. `flat.extend(row)` does the inner "
        "loop for you.",
    },
    {
        "n": 5,
        "title": "Only the palindromes",
        "ask": "Keep the words that read the same backwards.",
        "data": 'words = ["bob", "hello", "level", "python"]',
        "answer": "['bob', 'level']",
        "solution": [
            'words = ["bob", "hello", "level", "python"]',
            "found = []",
            "",
            "for w in words:",
            "    if w == w[::-1]:",
            "        found.append(w)",
            "",
            "print(found)",
        ],
        "note": "`w[::-1]` is a slice with step -1 — the whole string, walked "
        "backwards.",
    },
    {
        "n": 6,
        "title": "Rotate right",
        "ask": "Move every item 2 places to the right. What falls off the end "
        "comes back at the front.",
        "data": "numbers = [1, 2, 3, 4, 5]",
        "answer": "[4, 5, 1, 2, 3]",
        "solution": [
            "numbers = [1, 2, 3, 4, 5]",
            "k = 2",
            "",
            "print(numbers[-k:] + numbers[:-k])",
        ],
        "note": "Two slices and a `+`. `numbers[-2:]` is the tail, "
        "`numbers[:-2]` is everything before it.",
    },
    {
        "n": 7,
        "title": "Pairs that add to 10",
        "ask": "Print every pair of positions whose two numbers add up to 10. "
        "Use each pair once.",
        "data": "numbers = [2, 8, 3, 7, 5, 5]",
        "answer": "(2, 8)  (3, 7)  (5, 5)",
        "solution": [
            "numbers = [2, 8, 3, 7, 5, 5]",
            "",
            "for i in range(len(numbers)):",
            "    for j in range(i + 1, len(numbers)):",
            "        if numbers[i] + numbers[j] == 10:",
            "            print(numbers[i], numbers[j])",
        ],
        "note": "`range(i + 1, ...)` in the inner loop is what stops you "
        "finding every pair twice — and stops a number pairing with "
        "itself.",
    },
    {
        "n": 8,
        "title": "Column totals",
        "ask": "The grid is a list of rows. Print the total of each column.",
        "data": "grid = [[1, 2, 3],\n        [4, 5, 6],\n        [7, 8, 9]]",
        "answer": "[12, 15, 18]",
        "solution": [
            "grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]",
            "totals = []",
            "",
            "for c in range(3):",
            "    column = 0",
            "    for row in grid:",
            "        column = column + row[c]",
            "    totals.append(column)",
            "",
            "print(totals)",
        ],
        "note": "The outer loop walks *columns*, the inner one walks rows. "
        "`row[c]` picks one cell out of each row.",
    },
    {
        "n": 9,
        "title": "Turn it on its side",
        "ask": "Print the grid transposed: the first row becomes the first column.",
        "data": "grid = [[1, 2, 3],\n        [4, 5, 6],\n        [7, 8, 9]]",
        "answer": "[[1, 4, 7], [2, 5, 8], [3, 6, 9]]",
        "solution": [
            "grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]",
            "turned = []",
            "",
            "for c in range(3):",
            "    new_row = []",
            "    for row in grid:",
            "        new_row.append(row[c])",
            "    turned.append(new_row)",
            "",
            "print(turned)",
        ],
        "note": "Same shape as task 8, but you collect the cells instead of "
        "adding them up. Build `new_row` *inside* the outer loop.",
    },
    {
        "n": 10,
        "title": "The most common number",
        "ask": "Print the number that appears most often.",
        "data": "numbers = [4, 9, 2, 9, 7, 9, 4]",
        "answer": "9",
        "solution": [
            "numbers = [4, 9, 2, 9, 7, 9, 4]",
            "best = numbers[0]",
            "",
            "for n in numbers:",
            "    if numbers.count(n) > numbers.count(best):",
            "        best = n",
            "",
            "print(best)",
        ],
        "note": "`numbers.count(n)` says how many times `n` appears. Start "
        "`best` from the first item, never from 0.",
    },
]


# ================================================================== TITLE ==
def title_slide():
    s = prs.slides.add_slide(prs.slide_layouts[6])
    _box(s, 0, 0, W, H, fill=NAVY)
    _box(s, 0, H - Inches(0.28), W, Inches(0.28), fill=YELLOW)
    _box(s, M, Inches(1.5), Inches(0.12), Inches(1.5), fill=YELLOW)
    tf = _tf(s, M + Inches(0.4), Inches(1.4), Inches(10.5), Inches(2.0))
    _para(tf, "PYTHON · LISTS", 15, YELLOW, bold=True, first=True, space_after=12)
    _para(tf, "The Race", 56, WHITE, bold=True, space_after=10)
    _para(
        tf,
        "Ten list problems · first correct answer takes the point",
        22,
        RGBColor(0xA9, 0xBD, 0xD1),
    )
    tf2 = _tf(s, M + Inches(0.4), Inches(4.4), Inches(11.0), Inches(1.6))
    _para(
        tf2,
        "Laptops open. One problem at a time.",
        19,
        RGBColor(0x8F, 0xB6, 0xD9),
        first=True,
        space_after=8,
    )
    _para(
        tf2,
        "They get harder as we go — the last three are worth staying for.",
        19,
        RGBColor(0x8F, 0xB6, 0xD9),
    )
    tf3 = _tf(s, M + Inches(0.4), Inches(6.2), Inches(10.0), Inches(0.5))
    _para(
        tf3, "python-workbook2026  ·  lists", 13, RGBColor(0x6E, 0x8A, 0xA3), first=True
    )


def rules_slide():
    s = slide("How the race works", kicker="Rules", footer=False)
    bullets(
        s,
        [
            "Each problem goes on screen with the exact list to use",
            "Write it, run it, then raise your hand — *do not call the answer out*",
            "I check the screen. First one that is right takes the *+*",
            "The answer has to come from a program, not from your head",
            "",
            "Two or more right at once? Both get the point",
            "Nobody gets it in three minutes? We solve it together, nobody loses",
        ],
        y=BODY_TOP,
        size=19,
    )
    note(
        s,
        "The point is for a *working program*. A right number with no code "
        "behind it does not count — that is the whole exercise.",
        Inches(5.6),
        kind="ok",
    )

    s = slide("Score sheet", kicker="Keep your own count", footer=False)
    table(
        s,
        ["Problem", "Topic", "Who got it first"],
        [[f"{t['n']}", t["title"], ""] for t in TASKS],
        y=Inches(1.6),
        col_w=(1.2, 4.2, 5.4),
        size=14,
    )


# =================================================================== TASKS ==
def task_slide(t):
    s = slide(f"{t['n']}.  {t['title']}", kicker=f"Problem {t['n']} of 10")
    tf = _tf(s, M, BODY_TOP, Inches(7.0), Inches(1.6))
    _para(tf, t["ask"], 19, NAVY, first=True)

    code(
        s,
        t["data"].split("\n"),
        y=BODY_TOP + Inches(1.7),
        w=Inches(7.0),
        caption="use exactly this list",
    )

    out(
        s,
        [t["answer"]],
        x=M + Inches(7.4),
        y=BODY_TOP,
        w=Inches(4.8),
        label="Your program must print",
    )
    tf2 = _tf(s, M + Inches(7.4), BODY_TOP + Inches(1.5), Inches(4.8), Inches(2.0))
    _para(
        tf2, "First working program wins the point.", 17, GRAY, first=True, italic=True
    )
    return s


def solution_slide(t):
    s = slide(f"{t['n']}.  {t['title']}", kicker="Solution")
    code(s, t["solution"], w=Inches(7.4))
    out(s, [t["answer"]], x=M + Inches(7.8), y=BODY_TOP, w=Inches(4.4))
    tf = _tf(s, M + Inches(7.8), BODY_TOP + Inches(1.4), Inches(4.4), Inches(2.6))
    _para(tf, t["note"], 16, GRAY, first=True)
    return s


# ================================================================= CLOSING ==
def closing():
    s = prs.slides.add_slide(prs.slide_layouts[6])
    _box(s, 0, 0, W, H, fill=NAVY)
    _box(s, 0, H - Inches(0.28), W, Inches(0.28), fill=YELLOW)
    tf = _tf(s, Inches(1.3), Inches(1.6), Inches(10.7), Inches(3.4))
    _para(tf, "That is the race", 44, WHITE, bold=True, first=True, space_after=20)
    _para(
        tf,
        "Every one of these is a loop, a list you build up, and a "
        "condition. Nothing else.",
        22,
        RGBColor(0xC3, 0xD3, 0xE1),
        space_after=16,
    )
    _para(
        tf,
        "If a problem beat you today, write it again tonight without "
        "looking at the solution slide. That is where the learning is.",
        19,
        RGBColor(0x8F, 0xB6, 0xD9),
    )
    tf2 = _tf(s, Inches(1.3), Inches(5.3), Inches(10.7), Inches(1.2))
    _para(
        tf2, "uv run pytest lists/", 20, YELLOW, bold=True, first=True, space_after=10
    )
    _para(tf2, "See you next lesson", 20, YELLOW, bold=True)


# ==================================================================== main ==
title_slide()
rules_slide()

section(
    "The problems",
    "Ten of them, easiest first",
    ["One slide each", "Write it and run it", "Hand up when it works"],
)
for task in TASKS:
    task_slide(task)

section(
    "The solutions",
    "One way to do each — yours may differ",
    [
        "Shown after the race",
        "Compare with your own",
        "Different and working is still right",
    ],
)
for task in TASKS:
    solution_slide(task)

closing()

print(f"{save(OUT)} slides -> {OUT}")
