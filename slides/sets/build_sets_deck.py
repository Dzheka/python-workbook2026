"""Build the sets deck — "No Duplicates, No Waiting".

Introduces the set: what it is, how to change it, why `in` is fast (a small
hash-table picture that follows on from the "Names Are Arrows" lists deck),
set algebra with a Venn diagram, the everyday patterns and traps, and finally
the six exercises in `sets/`.

Every output on these slides was produced by running the code on CPython 3.13.
Sets of strings print in a different order on every run, so the slides print
sets of small integers, or wrap string sets in `sorted()`.

Run:  uv run --with python-pptx python slides/sets/build_sets_deck.py
"""

from pathlib import Path

from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN

from _deck import (
    BLUE,
    BODY_TOP,
    GRAY,
    GREEN,
    M,
    MONO,
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

OUT = Path(__file__).with_name("sets.pptx")

PALE = RGBColor(0xFA, 0xFB, 0xFC)
FADED = RGBColor(0xC9, 0xD2, 0xDB)
SOFT = RGBColor(0xA9, 0xBD, 0xD1)


def _i(v):
    return Inches(v)


def label(
    s,
    x,
    y,
    text,
    size=12,
    color=GRAY,
    w=3.0,
    align=PP_ALIGN.LEFT,
    bold=False,
    font=None,
):
    tf = _tf(s, _i(x), _i(y), _i(w), _i(0.4))
    if font:
        _para(tf, text, size, color, first=True, align=align, bold=bold, font=font)
    else:
        _para(tf, text, size, color, first=True, align=align, bold=bold)


def cell(s, x, y, w, h, text, fill=WHITE, line=BLUE, color=NAVY, size=16):
    shp = _box(s, _i(x), _i(y), _i(w), _i(h), fill=fill, line=line)
    tf = shp.text_frame
    tf.margin_left = tf.margin_right = 0
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    _para(
        tf, text, size, color, bold=True, font=MONO, first=True, align=PP_ALIGN.CENTER
    )
    return shp


def venn(s, x, y, left, both, right, shade=None, title=None, d=2.2, size=16):
    """Two overlapping circles. shade: subset of {"left", "both", "right"}."""
    shade = shade or set()
    off = d * 0.58
    for cx, side in ((x, "left"), (x + off, "right")):
        o = _box(
            s, _i(cx), _i(y), _i(d), _i(d), fill=None, line=BLUE, shape=MSO_SHAPE.OVAL
        )
        o.line.width = _i(0.025)
    regions = {
        "left": (x + 0.08, left),
        "both": (x + off - 0.02, both),
        "right": (x + d + 0.02, right),
    }
    rw = off - 0.1
    for key, (rx, text) in regions.items():
        hot = key in shade
        if hot:
            _box(
                s,
                _i(rx),
                _i(y + d / 2 - 0.3),
                _i(rw),
                _i(0.6),
                fill=YELLOW,
                shape=MSO_SHAPE.ROUNDED_RECTANGLE,
                radius=0.3,
            )
        label(
            s,
            rx,
            y + d / 2 - 0.17,
            text,
            size=size,
            color=NAVY if hot else GRAY,
            w=rw,
            align=PP_ALIGN.CENTER,
            bold=hot,
            font=MONO,
        )
    label(s, x, y - 0.32, "A", size=13, color=BLUE, bold=True, w=1)
    label(s, x + off + d - 0.4, y - 0.32, "B", size=13, color=BLUE, bold=True, w=1)
    if title:
        label(
            s,
            x - 0.2,
            y + d + 0.1,
            title,
            size=15,
            color=NAVY,
            bold=True,
            w=d + off + 0.4,
            align=PP_ALIGN.CENTER,
            font=MONO,
        )


# ================================================================== TITLE ==
def title_slide():
    s = prs.slides.add_slide(prs.slide_layouts[6])
    _box(s, 0, 0, W, H, fill=NAVY)
    _box(s, 0, H - Inches(0.28), W, Inches(0.28), fill=YELLOW)
    _box(s, M, Inches(1.5), Inches(0.12), Inches(1.5), fill=YELLOW)
    tf = _tf(s, M + Inches(0.4), Inches(1.4), Inches(10.5), Inches(2.0))
    _para(tf, "PYTHON · SETS", 15, YELLOW, bold=True, first=True, space_after=12)
    _para(tf, "No Duplicates, No Waiting", 52, WHITE, bold=True, space_after=10)
    _para(tf, "Sets: uniqueness, instant lookup and set algebra", 22, SOFT)
    tf2 = _tf(s, M + Inches(0.4), Inches(4.3), Inches(11.0), Inches(2.0))
    blue = RGBColor(0x8F, 0xB6, 0xD9)
    _para(
        tf2,
        "A list remembers order and keeps everything.",
        18,
        blue,
        first=True,
        space_after=8,
    )
    _para(
        tf2,
        "A set forgets order, keeps each thing once — and answers "
        "“is it here?” instantly.",
        18,
        blue,
    )
    tf3 = _tf(s, M + Inches(0.4), Inches(6.2), Inches(10.0), Inches(0.5))
    _para(
        tf3, "python-workbook2026  ·  sets", 13, RGBColor(0x6E, 0x8A, 0xA3), first=True
    )


def hook_slide():
    s = slide("Who came both days?", kicker="Two minutes", footer=False)
    code(
        s,
        [
            'day1 = ["Ali", "Sara", "Timur", "Nilu"]',
            'day2 = ["Sara", "Bek", "Nilu", "Ali"]',
            "",
            "# with lists: a loop, an `in`, an append...",
            "both = []",
            "for name in day1:",
            "    if name in day2:",
            "        both.append(name)",
        ],
        w=Inches(7.2),
    )
    tf = _tf(s, M + Inches(7.6), BODY_TOP, Inches(4.6), Inches(1.0))
    _para(tf, "With sets: one line.", 19, NAVY, bold=True, first=True)
    code(
        s,
        ["print(sorted(set(day1) & set(day2)))"],
        x=M + Inches(7.6),
        y=BODY_TOP + Inches(0.55),
        w=Inches(4.6),
        size=13,
    )
    out(
        s,
        ["['Ali', 'Nilu', 'Sara']"],
        x=M + Inches(7.6),
        y=BODY_TOP + Inches(1.5),
        w=Inches(4.6),
    )
    note(
        s,
        "By the end of today `&` will read as plainly as `+`, and you will know "
        "why the set version is also *much faster* on big lists.",
        Inches(5.9),
        kind="tip",
    )


def roadmap_slide():
    s = slide("What we cover today", kicker="Roadmap", footer=False)
    table(
        s,
        ["Part", "Topic", "You will be able to"],
        [
            ["1", "*What a set is*", "create one and name its three rules"],
            ["2", "*Changing a set*", "add, remove and loop without surprises"],
            ["3", "*Why `in` is instant*", "draw a hash table and explain the rules"],
            ["4", "*Set algebra*", "use `|  &  -  ^` and subset checks"],
            ["5", "*Patterns and traps*", "dedupe, track what you've seen, avoid bugs"],
            ["6", "*Your tasks*", "know what each exercise practises"],
        ],
        col_w=(0.8, 3.6, 7.0),
        size=16,
    )


# =================================================================== PART 1 ==
def part1():
    section(
        "What a set is",
        "A bag of unique things",
        ["Creating sets", "The {} trap", "Three rules"],
    )

    s = slide("Making a set", kicker="Syntax")
    code(
        s,
        [
            "print({3, 1, 3, 2, 1})           # curly braces",
            "print(set([2, 2, 3, 5, 5]))      # from a list",
            'print(sorted(set("mississippi")))  # from a string',
            'print(len(set("mississippi")))',
        ],
        w=Inches(7.6),
    )
    out(
        s,
        ["{1, 2, 3}", "{2, 3, 5}", "['i', 'm', 'p', 's']", "4"],
        x=M + Inches(8.0),
        y=BODY_TOP,
        w=Inches(3.9),
    )
    bullets(
        s,
        [
            "Duplicates vanish the moment the set is built",
            "`set(anything)` takes any iterable: a list, a string, a range…",
            "`len(set(x))` = how many *different* things are in `x`",
        ],
        y=Inches(3.9),
        size=18,
    )
    note(
        s,
        "We print `sorted(...)` for strings because a set of strings comes out "
        "in a different order every run. Part 3 shows why.",
        Inches(5.9),
        kind="tip",
    )

    s = slide("{} is not an empty set", kicker="Trap")
    code(
        s,
        ["print(type({}))", "print(type(set()))", "print(set() == {})"],
        w=Inches(6.4),
    )
    out(
        s,
        ["<class 'dict'>", "<class 'set'>", "False"],
        x=M + Inches(6.8),
        y=BODY_TOP,
        w=Inches(5.0),
    )
    note(
        s,
        "Curly braces were taken by dictionaries first. An *empty* set is always "
        "`set()`. `{1, 2}` with items in it is a set.",
        Inches(4.2),
        kind="warn",
    )

    s = slide("Three rules of a set", kicker="The whole idea")
    table(
        s,
        ["Rule", "So…", "Proof"],
        [
            ["*Unique*", "each value at most once", "`{3, 1, 3}` → `{1, 3}`"],
            [
                "*Unordered*",
                "no index, no slicing, no “first”",
                "`s[0]` → TypeError",
            ],
            [
                "*Immutable items only*",
                "numbers, strings, tuples — not lists",
                "`s.add([1, 2])` → TypeError",
            ],
        ],
        col_w=(2.8, 3.8, 4.8),
        size=15,
    )
    code(
        s,
        ["s = set()", "s.add((1, 2))     # a tuple is fine", "print(s)"],
        y=Inches(3.7),
        w=Inches(6.4),
    )
    out(s, ["{(1, 2)}"], x=M + Inches(6.8), y=Inches(3.7), w=Inches(5.0))
    note(
        s,
        "Last lesson: a tuple can never change. That is exactly why it may live "
        "in a set and a list may not — Part 3 explains.",
        Inches(5.8),
        kind="ok",
    )


# =================================================================== PART 2 ==
def part2():
    section(
        "Changing a set",
        "Add, remove, look inside",
        ["add", "remove vs discard", "Looping"],
    )

    s = slide("Adding and removing", kicker="Methods")
    code(
        s,
        [
            "s = {2, 3, 5}",
            "s.add(7)",
            "s.add(3)          # already there: nothing happens",
            "print(s)",
            "",
            "s.discard(11)     # not there: nothing happens",
            "print(s)",
            "s.remove(11)      # not there: error",
        ],
        w=Inches(7.2),
    )
    out(
        s,
        ["{2, 3, 5, 7}", "{2, 3, 5, 7}", "KeyError: 11"],
        x=M + Inches(7.6),
        y=BODY_TOP,
        w=Inches(4.6),
    )
    note(
        s,
        "Use `remove` when the item *must* be there (an error tells you about the "
        "bug). Use `discard` when “maybe” is fine.",
        Inches(5.9),
        kind="tip",
    )

    s = slide("The set methods you need", kicker="Cheat sheet")
    table(
        s,
        ["Method", "Does", "If the item is missing"],
        [
            ["`s.add(x)`", "puts `x` in", "—"],
            ["`s.remove(x)`", "takes `x` out", "*KeyError*"],
            ["`s.discard(x)`", "takes `x` out", "nothing"],
            ["`s.pop()`", "takes out *some* item and returns it", "KeyError if empty"],
            ["`s.clear()`", "empties the set", "—"],
            ["`x in s`", "True / False — instantly", "—"],
            ["`len(s)`", "how many items", "—"],
        ],
        col_w=(2.6, 5.4, 3.4),
        size=15,
    )
    note(
        s,
        "No `append`, no `insert`, no `sort` — a set has no positions to put "
        "things at.",
        Inches(5.4),
        kind="ok",
    )

    s = slide("Looping over a set", kicker="for")
    code(
        s,
        [
            "s = {2, 3, 5}",
            "print(sorted(s, reverse=True))",
            "print(5 in s, 4 in s)",
            "",
            "for x in sorted(s):     # sorted() gives a list",
            "    print(x)",
        ],
        w=Inches(7.0),
    )
    out(
        s,
        ["[5, 3, 2]", "True False", "2", "3", "5"],
        x=M + Inches(7.4),
        y=BODY_TOP,
        w=Inches(4.8),
    )
    note(
        s,
        "`for x in s` works, but in no promised order. When order matters — "
        "printing, tests — loop over `sorted(s)`.",
        Inches(5.6),
        kind="tip",
    )


# =================================================================== PART 3 ==
def part3():
    section(
        "Why in is instant",
        "A peek inside the hash table",
        [
            "List: check one by one",
            "Set: jump to the bucket",
            "Why lists are not allowed",
        ],
    )

    s = slide("A list checks one by one", kicker="x in my_list")
    cells = ["14", "7", "30", "2", "9", "21", "5", "11"]
    for i, v in enumerate(cells):
        hit = v == "5"
        cell(s, 0.9 + i * 0.95, 2.2, 0.95, 0.7, v, fill=YELLOW if hit else WHITE)
        label(
            s,
            0.9 + i * 0.95,
            2.95,
            f"{i + 1}",
            size=11,
            w=0.95,
            align=PP_ALIGN.CENTER,
            color=GREEN if hit else GRAY,
        )
    label(
        s,
        0.9,
        1.75,
        "5 in numbers   →   7 comparisons",
        size=16,
        color=NAVY,
        w=8,
        bold=True,
        font=MONO,
    )
    table(
        s,
        ["Items in the list", "Worst case for `x in list`", "For `x in set`"],
        [
            ["10", "10 checks", "about 1"],
            ["10 000", "10 000 checks", "about 1"],
            ["1 000 000", "1 000 000 checks", "about 1"],
        ],
        y=Inches(3.6),
        col_w=(3.2, 4.4, 3.8),
        size=16,
    )
    note(
        s,
        "A list has to look at every item until it finds a match. A set goes "
        "*straight to where the item would be*. How? Next slide.",
        Inches(5.65),
        kind="ok",
    )

    s = slide("A set is a row of buckets", kicker="Hashing")
    code(
        s,
        [
            "for n in [3, 10, 21]:",
            "    print(n, hash(n) % 8)",
            "",
            "print({3, 10, 21})",
        ],
        w=Inches(5.0),
    )
    out(s, ["3 3", "10 2", "21 5", "{10, 3, 21}"], y=Inches(3.45), w=Inches(5.0))
    label(
        s,
        6.2,
        1.75,
        "an empty set starts with 8 buckets",
        size=13,
        w=6,
        bold=True,
        color=BLUE,
    )
    contents = {2: "10", 3: "3", 5: "21"}
    for b in range(8):
        v = contents.get(b, "")
        cell(
            s,
            6.2 + b * 0.78,
            2.3,
            0.78,
            0.8,
            v,
            fill=YELLOW if v else PALE,
            line=BLUE if v else FADED,
        )
        label(s, 6.2 + b * 0.78, 3.15, str(b), size=11, w=0.78, align=PP_ALIGN.CENTER)
    tf = _tf(s, Inches(6.2), Inches(3.75), Inches(6.4), Inches(1.9))
    _para(
        tf,
        "hash(x) turns a value into a number.",
        16,
        NAVY,
        bold=True,
        first=True,
        space_after=6,
    )
    _para(
        tf,
        "% 8 picks a bucket. To check `21 in s` Python computes the bucket "
        "(5) and looks only there.",
        15,
        GRAY,
        space_after=6,
    )
    _para(tf, "Printing walks the buckets left to right — so {10, 3, 21}.", 15, GRAY)
    note(
        s,
        "Simplified — the real table grows and handles two items wanting the "
        "same bucket — but this is the whole idea: *compute where, look once.*",
        Inches(5.9),
        kind="tip",
    )

    s = slide("Why a list cannot go in a set", kicker="Hashable")
    bullets(
        s,
        [
            "A value's bucket is computed from its contents when it goes in",
            "If those contents could change later, the value would sit in the *wrong "
            "bucket* — and `in` would never find it again",
            "So Python only lets in values that can never change: numbers, strings, "
            "tuples, frozensets",
            "That is what *hashable* means: the hash can never change",
        ],
        size=18,
        gap=12,
    )
    code(s, ["s.add([1, 2])"], y=Inches(4.85), w=Inches(5.0))
    out(
        s,
        ["TypeError: unhashable type: 'list'"],
        x=M + Inches(5.4),
        y=Inches(4.85),
        w=Inches(6.5),
        label="What you get",
    )
    note(
        s,
        "The set *itself* is mutable — you can add and remove. Only its "
        "*items* must be immutable.",
        Inches(6.0),
        kind="warn",
    )


# =================================================================== PART 4 ==
def part4():
    section(
        "Set algebra",
        "Combine and compare in one symbol",
        ["| & - ^", "Subset and superset", "In-place versions"],
    )

    s = slide("Four operators", kicker="A = {2, 3, 5}   B = {3, 5, 7}")
    specs = [
        ("A | B", {"left", "both", "right"}, "{2, 3, 5, 7}", "in either"),
        ("A & B", {"both"}, "{3, 5}", "in both"),
        ("A - B", {"left"}, "{2}", "in A, not in B"),
        ("A ^ B", {"left", "right"}, "{2, 7}", "in exactly one"),
    ]
    for i, (op, shade, result, words) in enumerate(specs):
        x = 0.75 + i * 3.1
        venn(s, x, 2.3, "2", "3 5", "7", shade=shade, d=1.6, size=14)
        label(
            s,
            x - 0.1,
            4.05,
            op,
            size=20,
            color=NAVY,
            bold=True,
            w=2.9,
            align=PP_ALIGN.CENTER,
            font=MONO,
        )
        label(
            s,
            x - 0.1,
            4.5,
            result,
            size=16,
            color=BLUE,
            w=2.9,
            align=PP_ALIGN.CENTER,
            font=MONO,
        )
        label(s, x - 0.1, 4.9, words, size=13, color=GRAY, w=2.9, align=PP_ALIGN.CENTER)
    note(
        s,
        "Every result was printed by Python. `-` is the only one where order "
        "matters: `B - A` is `{7}`.",
        Inches(5.75),
        kind="ok",
    )

    s = slide("Operators and their method names", kicker="Same thing, two spellings")
    table(
        s,
        ["Operator", "Method", "Meaning"],
        [
            ["`a | b`", "`a.union(b)`", "everything in either"],
            ["`a & b`", "`a.intersection(b)`", "only what both have"],
            ["`a - b`", "`a.difference(b)`", "what `a` has and `b` does not"],
            ["`a ^ b`", "`a.symmetric_difference(b)`", "in one, not both"],
        ],
        col_w=(2.2, 4.6, 4.6),
        size=16,
    )
    note(
        s,
        "Operators need *two sets*. Methods accept any iterable: "
        "`a.union([7, 11])` works, `a | [7, 11]` is a TypeError.",
        Inches(4.3),
        kind="tip",
    )

    s = slide("Comparing sets", kicker="Subset, superset, disjoint")
    code(
        s,
        [
            "print({2, 3} <= {2, 3, 5, 7})     # subset",
            "print({2, 3} < {2, 3})            # proper subset",
            "print({2, 3, 5, 7} >= {3})        # superset",
            "print({2, 3}.isdisjoint({5, 7}))  # nothing shared",
        ],
        w=Inches(7.8),
    )
    out(
        s,
        ["True", "False", "True", "True"],
        x=M + Inches(8.2),
        y=BODY_TOP,
        w=Inches(3.7),
    )
    bullets(
        s,
        [
            "`a <= b` — every item of `a` is also in `b`",
            "`a < b` — the same, *and* `b` has something extra",
            "`a.isdisjoint(b)` — `a & b` would be empty",
        ],
        y=Inches(4.0),
        size=18,
    )
    note(
        s,
        "On sets, `<` and `>` do *not* compare sizes. `{9} < {1, 2}` is False.",
        Inches(6.0),
        kind="warn",
    )

    s = slide("Change the set in place", kicker="|=  &=  -=  ^=")
    code(
        s,
        [
            "a = {2, 3, 5}",
            "a |= {7, 11}      # add all of these",
            "print(a)",
            "a -= {2, 3}       # remove all of these",
            "print(a)",
        ],
        w=Inches(7.0),
    )
    out(
        s,
        ["{2, 3, 5, 7, 11}", "{5, 7, 11}"],
        x=M + Inches(7.4),
        y=BODY_TOP,
        w=Inches(4.8),
    )
    note(
        s,
        "Like a list's `+=`, these change the *same* set object — every name "
        "pointing at it sees the change. (Remember: names are arrows.)",
        Inches(4.6),
        kind="ok",
    )


# =================================================================== PART 5 ==
def part5():
    section(
        "Patterns and traps",
        "What sets are actually used for",
        [
            "Remove duplicates",
            "The seen-set",
            "Set comprehensions",
            "Changing while looping",
            "frozenset",
        ],
    )

    s = slide("Removing duplicates", kicker="Pattern 1")
    code(
        s,
        [
            "nums = [3, 1, 3, 2, 1]",
            "",
            "print(list(set(nums)))         # order NOT kept",
            "print(list(dict.fromkeys(nums)))  # order kept",
        ],
        w=Inches(7.6),
    )
    out(s, ["[1, 2, 3]", "[3, 1, 2]"], x=M + Inches(8.0), y=BODY_TOP, w=Inches(3.9))
    note(
        s,
        "`[1, 2, 3]` *looks* sorted only because small numbers land in buckets "
        "1, 2, 3. Never rely on it. Need the original order? Use a seen-set.",
        Inches(3.9),
        kind="warn",
    )

    s = slide("The seen-set", kicker="Pattern 2 — the one you'll use most")
    code(
        s,
        [
            "seen = set()",
            'for w in ["red", "blue", "green", "blue", "red"]:',
            "    if w in seen:",
            '        print("first repeat:", w)',
            "        break",
            "    seen.add(w)",
        ],
        w=Inches(7.6),
    )
    out(s, ["first repeat: blue"], x=M + Inches(8.0), y=BODY_TOP, w=Inches(3.9))
    bullets(
        s,
        [
            "Walk the data once; ask the set “have I met this before?”",
            "Each check is instant, so the whole loop stays fast",
            "Three of today's tasks are this pattern in disguise",
        ],
        y=Inches(4.15),
        size=18,
    )

    s = slide("Set comprehensions", kicker="Pattern 3")
    code(
        s,
        [
            "print({x * x for x in [-2, -1, 0, 1, 2]})",
            "",
            "s = {1, 2, 3, 4, 5}",
            "s = {x for x in s if x % 2 != 0}",
            "print(s)",
        ],
        w=Inches(7.6),
    )
    out(s, ["{0, 1, 4}", "{1, 3, 5}"], x=M + Inches(8.0), y=BODY_TOP, w=Inches(3.9))
    note(
        s,
        "Exactly like a list comprehension, with curly braces — and duplicates "
        "(`(-2)² = 2²`) disappear on their own.",
        Inches(4.3),
        kind="tip",
    )

    s = slide("Don't change a set while looping over it", kicker="Trap")
    code(
        s,
        [
            "s = {1, 2, 3, 4, 5}",
            "for x in s:",
            "    if x % 2 == 0:",
            "        s.remove(x)",
        ],
        w=Inches(6.4),
    )
    out(
        s,
        ["RuntimeError: Set changed size", "during iteration"],
        x=M + Inches(6.8),
        y=BODY_TOP,
        w=Inches(5.0),
        label="What you get",
    )
    code(
        s,
        [
            "s = {x for x in s if x % 2 != 0}   # build a new set instead",
        ],
        y=Inches(3.75),
        w=Inches(9.0),
    )
    note(
        s,
        "Removing an item moves things between buckets mid-walk, so Python "
        "stops you. Build a new set, or loop over `s.copy()`.",
        Inches(5.0),
        kind="warn",
    )

    s = slide("frozenset: a set that cannot change", kicker="Bonus")
    code(
        s,
        [
            "key = frozenset({2, 3})",
            'd = {key: "pair"}',
            "print(d[frozenset({3, 2})])",
            "",
            "key.add(5)",
        ],
        w=Inches(6.6),
    )
    out(
        s,
        ["pair", "", "AttributeError: 'frozenset'", "object has no attribute 'add'"],
        x=M + Inches(7.0),
        y=BODY_TOP,
        w=Inches(5.0),
    )
    note(
        s,
        "*set* is to *frozenset* what *list* is to *tuple*. Use it when a group "
        "of things must be a dict key or live inside another set.",
        Inches(4.6),
        kind="ok",
    )


# =================================================================== PART 6 ==
def part6():
    section(
        "Your tasks",
        "Six exercises in sets/",
        ["What each one practises", "One special rule", "How to check"],
    )

    s = slide("Six exercises, easiest first", kicker="sets/")
    table(
        s,
        ["Exercise", "Level", "What it practises"],
        [
            [
                "`set_operations`",
                "start here",
                "build `|  &  ^  <=` yourself with `add` and `in`",
            ],
            ["`remove_duplicate_letters`", "medium", "the seen-set, keeping order"],
            ["`find_missing_numbers`", "medium", "`set(range(...)) - set(numbers)`"],
            ["`pangram_checker`", "medium", "is the alphabet a subset of the text?"],
            ["`isogram`", "medium", "the seen-set, ignoring case, spaces, hyphens"],
            [
                "`longest_consecutive`",
                "hard",
                "instant `in` makes an O(n) solution possible — read the hint",
            ],
        ],
        col_w=(3.6, 1.6, 6.2),
        size=15,
    )
    note(
        s,
        "Read `sets/_docs/` first — set_basics, then set_operations, then "
        "set_best_practices.",
        Inches(5.4),
        kind="tip",
    )

    s = slide("set_operations has a rule", kicker="No shortcuts")
    bullets(
        s,
        [
            "You write `uniques`, `union`, `intersection`, `is_subset`, `symmetric_diff`",
            "Only `set()`, `.add()`, `for` and `in` are allowed inside your functions",
            "No `| & - ^ <= < >= >`, no `.union()` and friends, no `{...}` literals",
            "The test *reads your source code* and fails if it finds a shortcut",
        ],
        size=17,
        gap=8,
    )
    code(
        s,
        [
            "def intersection(set1, set2):",
            "    result = set()",
            "    for x in set1:",
            "        ...           # your turn",
            "    return result",
        ],
        y=Inches(3.95),
        w=Inches(7.0),
        size=14,
    )
    note(
        s,
        "Once you have built `&` with a loop, you will never forget what it does.",
        Inches(6.05),
        kind="ok",
    )

    s = slide("Checking your work", kicker="Same as always")
    code(
        s,
        [
            "uv run pytest sets/isogram/      # one exercise",
            "uv run pytest sets/              # the whole topic",
        ],
        w=Inches(9.0),
    )
    bullets(
        s,
        [
            "Create `sets/isogram/isogram.py` next to the statement — name matches the "
            "folder",
            "*skipped* means the file is missing — skipped is not passed",
            "Push to your fork; the grader runs on your pull request",
        ],
        y=Inches(3.2),
        size=18,
    )


# ================================================================= CLOSING ==
def closing():
    s = prs.slides.add_slide(prs.slide_layouts[6])
    _box(s, 0, 0, W, H, fill=NAVY)
    _box(s, 0, H - Inches(0.28), W, Inches(0.28), fill=YELLOW)
    tf = _tf(s, Inches(1.3), Inches(1.2), Inches(10.7), Inches(4.2))
    _para(tf, "Reach for a set when…", 42, WHITE, bold=True, first=True, space_after=22)
    soft = RGBColor(0xC3, 0xD3, 0xE1)
    for line in [
        "…you need each thing once — duplicates vanish.",
        "…you ask “is it here?” over and over — the answer is instant.",
        "…you compare two groups — | & - ^ say it in one symbol.",
    ]:
        _para(tf, line, 22, soft, space_after=14)
    tf2 = _tf(s, Inches(1.3), Inches(5.4), Inches(10.7), Inches(1.0))
    _para(
        tf2,
        "And when order matters: sorted(), or keep a list beside it.",
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
part6()
closing()

print(f"{save(OUT)} slides -> {OUT}")
