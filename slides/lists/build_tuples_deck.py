"""Build the "Can It Change?" deck — lists, tuples and mutability.

A follow-up to the lists deck. It answers the question that bites everyone
exactly once: which values can be changed in place, which cannot, and why the
list you handed to a function came back different.

Covers mutable vs immutable types, tuples and why they exist, unpacking,
aliasing and copying, the mutable default argument, and the tuple that holds
a list.

Every output on these slides was produced by running the code.

Run:  uv run --with python-pptx python slides/lists/build_tuples_deck.py
"""

from pathlib import Path

from _deck import (
    BLUE,
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

OUT = Path(__file__).with_name("tuples.pptx")


# ================================================================== TITLE ==
def title_slide():
    s = prs.slides.add_slide(prs.slide_layouts[6])
    _box(s, 0, 0, W, H, fill=NAVY)
    _box(s, 0, H - Inches(0.28), W, Inches(0.28), fill=YELLOW)
    _box(s, M, Inches(1.5), Inches(0.12), Inches(1.5), fill=YELLOW)
    tf = _tf(s, M + Inches(0.4), Inches(1.4), Inches(10.5), Inches(2.0))
    _para(
        tf, "PYTHON · LISTS, PART 2", 15, YELLOW, bold=True, first=True, space_after=12
    )
    _para(tf, "Can It Change?", 52, WHITE, bold=True, space_after=10)
    _para(
        tf,
        "Lists, tuples, and the one idea behind both",
        22,
        RGBColor(0xA9, 0xBD, 0xD1),
    )
    tf2 = _tf(s, M + Inches(0.4), Inches(4.3), Inches(11.0), Inches(2.0))
    _para(
        tf2,
        "Two values can look identical and behave nothing alike.",
        18,
        RGBColor(0x8F, 0xB6, 0xD9),
        first=True,
        space_after=8,
    )
    _para(
        tf2,
        "By the end of today you will know which is which, and why it matters.",
        18,
        RGBColor(0x8F, 0xB6, 0xD9),
    )
    tf3 = _tf(s, M + Inches(0.4), Inches(6.2), Inches(10.0), Inches(0.5))
    _para(
        tf3, "python-workbook2026  ·  lists", 13, RGBColor(0x6E, 0x8A, 0xA3), first=True
    )


def hook_slide():
    s = slide("Find the bug", kicker="Two minutes", footer=False)
    code(
        s,
        [
            "def add_bonus(scores):",
            "    scores.append(100)",
            "    return scores",
            "",
            "my_scores = [50, 60]",
            "final = add_bonus(my_scores)",
            "",
            "print(final)",
            "print(my_scores)        # <- we never touched this one",
        ],
        w=Inches(7.0),
    )
    out(
        s,
        ["[50, 60, 100]", "[50, 60, 100]"],
        x=M + Inches(7.4),
        y=BODY_TOP,
        w=Inches(4.8),
    )
    tf = _tf(s, M + Inches(7.4), BODY_TOP + Inches(2.2), Inches(4.8), Inches(2.0))
    _para(tf, "my_scores changed too.", 19, NAVY, bold=True, first=True, space_after=10)
    _para(
        tf,
        "Nobody asked it to. No line in the program says my_scores.append.",
        16,
        GRAY,
    )
    note(
        s,
        "By the end of this lesson you will be able to explain this in one "
        "sentence — and fix it in one line.",
        Inches(6.0),
        kind="tip",
    )


def roadmap_slide():
    s = slide("What we cover today", kicker="Roadmap", footer=False)
    table(
        s,
        ["Part", "Topic", "You will be able to"],
        [
            ["1", "*Mutable or not*", "say which types can change in place"],
            ["2", "*Tuples*", "write one, unpack it, and say why it exists"],
            ["3", "*Two names, one list*", "explain the bug from slide 2"],
            ["4", "*Copying properly*", "pass a list without losing it"],
            ["5", "*Three classic traps*", "spot them before they bite"],
        ],
        y=BODY_TOP,
        col_w=(0.8, 3.4, 7.0),
        size=16,
    )
    note(
        s,
        "Everything today rests on one question you can ask about any "
        "value: *can this be changed in place, or not?*",
        Inches(5.2),
        kind="ok",
    )


# =================================================================== PART 1 ==
def part1():
    section(
        "Mutable or not",
        "The one question to ask about any value",
        ["The two camps", "Strings cannot change", "The same box, or a new one"],
    )

    s = slide("Two camps", kicker="Mutable vs immutable")
    table(
        s,
        ["Can be changed in place", "Cannot be changed, ever"],
        [
            ["`list`   [1, 2, 3]", "`int`   42"],
            ['`dict`   {"a": 1}', "`float`   3.14"],
            ["`set`   {1, 2}", '`str`   "hello"'],
            ["", "`tuple`   (1, 2, 3)"],
            ["", "`bool`   True"],
        ],
        col_w=(5.0, 5.0),
        size=17,
    )
    note(
        s,
        "*Mutable* means you can change the contents and it stays the same "
        'object. *Immutable* means the only way to "change" it is to '
        "build a new one.",
        Inches(4.9),
        kind="ok",
    )

    s = slide("A string cannot be edited", kicker="Immutable")
    y = code(
        s,
        [
            'word = "hello"',
            'word[0] = "H"',
        ],
        w=Inches(6.2),
    )
    out(
        s,
        ["TypeError: 'str' object does not", "support item assignment"],
        x=M + Inches(6.6),
        y=BODY_TOP,
        w=Inches(5.2),
        label="What you get",
    )
    y = code(
        s,
        [
            'word = "hello"',
            'word = "H" + word[1:]     # build a NEW string',
            "print(word)",
        ],
        y=y + Inches(0.1),
        w=Inches(6.2),
    )
    out(s, ["Hello"], x=M + Inches(6.6), y=BODY_TOP + Inches(1.9), w=Inches(5.2))
    note(
        s,
        "The second one works because it does not edit the string — it "
        "makes a new one and points the name at it.",
        Inches(5.9),
        kind="tip",
    )

    s = slide("Same box, or a new box?", kicker="id() tells you")
    code(
        s,
        [
            "numbers = [1, 2]",
            "print(id(numbers))",
            "numbers.append(3)",
            "print(id(numbers))    # the SAME number",
            "",
            'text = "ab"',
            "print(id(text))",
            'text = text + "c"',
            "print(id(text))       # a DIFFERENT number",
        ],
        w=Inches(7.2),
    )
    tf = _tf(s, M + Inches(7.6), BODY_TOP, Inches(4.6), Inches(3.4))
    _para(tf, "The list stayed put.", 19, NAVY, bold=True, first=True, space_after=6)
    _para(
        tf,
        "append changed what is inside the box. Anyone else holding that "
        "box sees the change.",
        16,
        GRAY,
        space_after=16,
    )
    _para(tf, "The string moved.", 19, NAVY, bold=True, space_after=6)
    _para(
        tf,
        'The old "ab" is untouched; the name now points somewhere '
        "else. Nobody else notices.",
        16,
        GRAY,
    )
    note(
        s,
        "`id()` is the object's address. Same id = same object. This single "
        "idea explains every surprise in the rest of the lesson.",
        Inches(6.0),
        kind="ok",
    )


# =================================================================== PART 2 ==
def part2():
    section(
        "Tuples",
        "A list that promised not to change",
        ["Writing one", "The comma that matters", "Unpacking", "Why they exist"],
    )

    s = slide("A tuple is a list that cannot change", kicker="Syntax")
    code(
        s,
        [
            "point = (3, 4)          # round brackets",
            "print(point[0])         # indexing works",
            "print(len(point))       # len works",
            "for value in point:     # looping works",
            "    print(value)",
            "",
            "point[0] = 9            # this does not",
        ],
        w=Inches(7.0),
    )
    out(
        s,
        [
            "3",
            "2",
            "3",
            "4",
            "",
            "TypeError: 'tuple' object does",
            "not support item assignment",
        ],
        x=M + Inches(7.4),
        y=BODY_TOP,
        w=Inches(4.8),
    )
    note(
        s,
        "Everything that *reads* a list works on a tuple. Everything that "
        "*changes* it is gone.",
        Inches(6.1),
        kind="ok",
    )

    s = slide("The comma is what makes it", kicker="Watch out")
    code(
        s,
        [
            "a = (5)       # just a number in brackets",
            "b = (5,)      # a tuple with one item",
            "",
            "print(type(a))",
            "print(type(b))",
        ],
        w=Inches(6.6),
    )
    out(
        s,
        ["<class 'int'>", "<class 'tuple'>"],
        x=M + Inches(7.0),
        y=BODY_TOP,
        w=Inches(5.0),
    )
    bullets(
        s,
        [
            "It is the *comma* that builds a tuple, not the brackets",
            "`point = 3, 4` is a tuple too — brackets are optional",
            "But write the brackets anyway; everyone reading your code will thank you",
        ],
        y=Inches(4.3),
        size=18,
    )
    note(
        s,
        "A one-item tuple without the comma is the single most common "
        "tuple bug. `(5)` is five. `(5,)` is a tuple.",
        Inches(6.0),
        kind="warn",
    )

    s = slide("Unpacking: the best part", kicker="Tuples at work")
    code(
        s,
        [
            "point = (3, 4)",
            "x, y = point            # two names at once",
            "",
            "a, b = 1, 2",
            "a, b = b, a             # swap, no temp variable",
            "",
            "def min_max(numbers):",
            "    return min(numbers), max(numbers)",
            "",
            "low, high = min_max([4, 9, 2])",
        ],
        w=Inches(7.2),
    )
    tf = _tf(s, M + Inches(7.6), BODY_TOP + Inches(0.2), Inches(4.6), Inches(3.6))
    _para(tf, "x = 3, y = 4", 17, BLUE, bold=True, first=True, space_after=14)
    _para(tf, "a = 2, b = 1", 17, BLUE, bold=True, space_after=14)
    _para(tf, "low = 2, high = 9", 17, BLUE, bold=True, space_after=18)
    _para(
        tf,
        "A function that returns two things is returning one tuple — you "
        "have been using tuples all along.",
        16,
        GRAY,
    )
    note(
        s,
        "`a, b = b, a` is the Python way to swap. The right-hand side "
        "becomes a tuple first, so nothing is overwritten half-way.",
        Inches(6.0),
        kind="tip",
    )

    s = slide("So why would anyone want less?", kicker="Why tuples exist")
    table(
        s,
        ["Reason", "What it looks like"],
        [
            [
                "A record whose shape is fixed",
                "`(latitude, longitude)` — a point has exactly two parts",
            ],
            [
                "Safe to hand around",
                "nobody you pass it to can change it behind your back",
            ],
            [
                "Can be a dictionary key",
                '`{(0, 0): "start"}` works; a list key is an error',
            ],
            ["Smaller and faster", "`(1, 2, 3)` is 64 bytes, `[1, 2, 3]` is 120"],
            [
                "Says what you mean",
                "a reader sees at a glance that this will not change",
            ],
        ],
        col_w=(3.6, 6.8),
        size=15,
    )
    note(
        s,
        "Rule of thumb: *many of the same thing* that grows and shrinks is "
        "a list. *A few different things* that belong together is a tuple.",
        Inches(5.3),
        kind="ok",
    )

    s = slide("Only two methods", kicker="list vs tuple")
    code(
        s,
        [
            "# everything a list can do to itself",
            "append  clear  copy  count  extend  index",
            "insert  pop  remove  reverse  sort",
            "",
            "# everything a tuple can do to itself",
            "count  index",
        ],
        w=Inches(8.0),
        dark=False,
    )
    tf = _tf(s, M + Inches(8.4), BODY_TOP + Inches(0.3), Inches(3.8), Inches(2.6))
    _para(
        tf,
        "Nine of the eleven list methods change the list.",
        17,
        NAVY,
        bold=True,
        first=True,
        space_after=10,
    )
    _para(tf, "A tuple keeps only the two that just look.", 16, GRAY)
    note(
        s,
        "You do not have to memorise this. Ask instead: does this method "
        "change the thing? Then a tuple will not have it.",
        Inches(5.4),
        kind="tip",
    )


# =================================================================== PART 3 ==
def part3():
    section(
        "Two names, one list",
        "Back to the bug from the start",
        ["b = a does not copy", "What a function receives", "Solving slide 2"],
    )

    s = slide("b = a does not make a copy", kicker="Aliasing")
    code(
        s,
        [
            "a = [1, 2, 3]",
            "b = a            # NOT a copy",
            "b.append(4)",
            "",
            "print(a)",
            "print(b)",
            "print(a is b)",
        ],
        w=Inches(6.4),
    )
    out(
        s,
        ["[1, 2, 3, 4]", "[1, 2, 3, 4]", "True"],
        x=M + Inches(6.8),
        y=BODY_TOP,
        w=Inches(5.0),
    )
    bullets(
        s,
        [
            "`b = a` copies the *label*, not the list",
            "One list now has two names, and either name can change it",
            '`a is b` asks "the same object?" — `a == b` only asks "same contents?"',
        ],
        y=Inches(4.4),
        size=18,
    )
    note(
        s,
        "This is only dangerous because lists are mutable. Do the same "
        "with a number or a string and nothing can go wrong.",
        Inches(6.1),
        kind="warn",
    )

    s = slide(
        "A function gets the list, not a photo of it", kicker="Why the bug happened"
    )
    code(
        s,
        [
            "def add_bonus(scores):",
            "    scores.append(100)      # changes the caller's list",
            "",
            "def add_bonus_safe(scores):",
            "    scores = scores + [100]  # builds a NEW list, caller unaffected",
            "",
            "my = [50, 60]",
            "add_bonus(my);       print(my)",
            "my = [50, 60]",
            "add_bonus_safe(my);  print(my)",
        ],
        w=Inches(7.6),
    )
    out(s, ["[50, 60, 100]", "[50, 60]"], x=M + Inches(8.0), y=BODY_TOP, w=Inches(4.2))
    note(
        s,
        "`append` changes the box. `scores + [100]` makes a new box and "
        "points the local name at it — the caller still holds the old one.",
        Inches(6.0),
        kind="ok",
    )


# =================================================================== PART 4 ==
def part4():
    section(
        "Copying properly",
        "Four ways, and when a copy is not enough",
        ["copy, slice, list()", "Shallow means one level"],
    )

    s = slide("Three ways to copy a list", kicker="All the same")
    code(
        s,
        [
            "a = [1, 2, 3]",
            "",
            "b = a.copy()",
            "c = a[:]",
            "d = list(a)",
            "",
            "b.append(4)",
            "print(a)        # a is untouched",
        ],
        w=Inches(6.4),
    )
    out(s, ["[1, 2, 3]"], x=M + Inches(6.8), y=BODY_TOP, w=Inches(5.0))
    tf = _tf(s, M + Inches(6.8), BODY_TOP + Inches(1.3), Inches(5.0), Inches(2.4))
    _para(
        tf, "Pick one and stick to it.", 18, NAVY, bold=True, first=True, space_after=8
    )
    _para(
        tf,
        "`a.copy()` says what it means, so prefer that one. `a[:]` is "
        "older code you will meet.",
        16,
        GRAY,
    )
    note(
        s,
        "A tuple needs none of this. There is nothing to protect it from.",
        Inches(5.9),
        kind="tip",
    )

    s = slide("A copy only goes one level deep", kicker="Shallow copy")
    code(
        s,
        [
            "grid = [[1, 2], [3, 4]]",
            "copy = grid.copy()",
            "",
            "copy.append([5, 6])    # the outer list is separate",
            "copy[0].append(99)     # the inner lists are NOT",
            "",
            "print(grid)",
        ],
        w=Inches(7.0),
    )
    out(s, ["[[1, 99], [3, 4]]"], x=M + Inches(7.4), y=BODY_TOP, w=Inches(4.8))
    note(
        s,
        "`copy()` makes a new outer list holding *the same inner lists*. "
        "For a grid you need a copy of every row — a loop, or "
        "`copy.deepcopy`.",
        Inches(5.6),
        kind="warn",
    )


# =================================================================== PART 5 ==
def part5():
    section(
        "Three classic traps",
        "Each one costs somebody a day",
        ["The default argument", "The tuple with a list inside", "== versus is"],
    )

    s = slide("Trap 1: the default that remembers", kicker="Mutable default")
    code(
        s,
        [
            "def collect(item, box=[]):     # the trap",
            "    box.append(item)",
            "    return box",
            "",
            'print(collect("a"))',
            'print(collect("b"))',
            'print(collect("c"))',
        ],
        w=Inches(7.0),
    )
    out(
        s,
        ["['a']", "['a', 'b']", "['a', 'b', 'c']"],
        x=M + Inches(7.4),
        y=BODY_TOP,
        w=Inches(4.8),
    )
    code(
        s,
        [
            "def collect(item, box=None):   # the fix",
            "    if box is None:",
            "        box = []",
            "    box.append(item)",
            "    return box",
        ],
        y=Inches(4.3),
        w=Inches(7.0),
    )
    note(
        s,
        "The default list is built *once*, when the `def` line runs — not "
        "on every call. So every call shares it.",
        Inches(6.2),
        kind="warn",
    )

    s = slide("Trap 2: a tuple holding a list", kicker="Immutable, sort of")
    code(
        s,
        [
            "t = (1, [2, 3])",
            "",
            "t[1].append(4)     # allowed!",
            "print(t)",
            "",
            "t[0] = 9           # still not allowed",
        ],
        w=Inches(6.6),
    )
    out(
        s,
        [
            "(1, [2, 3, 4])",
            "",
            "TypeError: 'tuple' object does",
            "not support item assignment",
        ],
        x=M + Inches(7.0),
        y=BODY_TOP,
        w=Inches(5.0),
    )
    note(
        s,
        "The tuple promises that *its slots* never change. It promises "
        "nothing about what lives in them. Slot 1 still holds the same "
        "list — that list just grew.",
        Inches(5.7),
        kind="ok",
    )

    s = slide("Trap 3: == is not is", kicker="Equal or identical")
    code(
        s,
        [
            "a = [1, 2, 3]",
            "b = [1, 2, 3]",
            "c = a",
            "",
            "print(a == b)    # same contents?",
            "print(a is b)    # same object?",
            "print(a is c)",
        ],
        w=Inches(6.4),
    )
    out(s, ["True", "False", "True"], x=M + Inches(6.8), y=BODY_TOP, w=Inches(5.0))
    bullets(
        s,
        [
            "Use `==` almost always — you care about the contents",
            "Use `is` for `None`: `if box is None:`",
            'If `a is b` is True, changing one changes "both"',
        ],
        y=Inches(4.5),
        size=18,
    )


# ================================================================= CLOSING ==
def closing():
    s = prs.slides.add_slide(prs.slide_layouts[6])
    _box(s, 0, 0, W, H, fill=NAVY)
    _box(s, 0, H - Inches(0.28), W, Inches(0.28), fill=YELLOW)
    tf = _tf(s, Inches(1.3), Inches(1.3), Inches(10.7), Inches(3.8))
    _para(
        tf, "One question, every time", 42, WHITE, bold=True, first=True, space_after=20
    )
    _para(tf, "Can this value be changed in place?", 26, YELLOW, space_after=18)
    _para(
        tf,
        "If yes, it is a list, a dict or a set — and anyone holding it "
        "can change it under you.",
        19,
        RGBColor(0xC3, 0xD3, 0xE1),
        space_after=10,
    )
    _para(
        tf,
        "If no, it is a number, a string or a tuple — and you can pass "
        "it anywhere without a worry.",
        19,
        RGBColor(0xC3, 0xD3, 0xE1),
    )
    tf2 = _tf(s, Inches(1.3), Inches(5.4), Inches(10.7), Inches(1.2))
    _para(
        tf2,
        "Now the practice round — first correct answer takes the point.",
        20,
        YELLOW,
        bold=True,
        first=True,
    )


# ==================================================================== main ==
title_slide()
hook_slide()
roadmap_slide()
part1()
part2()
part3()
part4()
part5()
closing()

print(f"{save(OUT)} slides -> {OUT}")
