"""Build the dicts deck — "Name It, Find It".

Introduces the dictionary: what it is, how to read and change it, how to loop
over it, the four everyday patterns (count, group, look up, remember-what-you-
saw), the traps, and finally the fourteen exercises in `dicts/`.

Every output on these slides was produced by running the code on CPython 3.13.
Dicts keep insertion order, so unlike the sets deck nothing here needs
`sorted()` to print the same way every run.

Run:  uv run --with python-pptx python slides/dicts/build_dicts_deck.py
"""

from pathlib import Path

from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN

from _deck import (
    BLUE,
    BODY_TOP,
    GRAY,
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

OUT = Path(__file__).with_name("dicts.pptx")

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


def arrow(s, x, y, w):
    a = _box(s, _i(x), _i(y), _i(w), _i(0.36), fill=BLUE, shape=MSO_SHAPE.RIGHT_ARROW)
    a.line.fill.background()


# ================================================================== TITLE ==
def title_slide():
    s = prs.slides.add_slide(prs.slide_layouts[6])
    _box(s, 0, 0, W, H, fill=NAVY)
    _box(s, 0, H - Inches(0.28), W, Inches(0.28), fill=YELLOW)
    _box(s, M, Inches(1.5), Inches(0.12), Inches(1.5), fill=YELLOW)
    tf = _tf(s, M + Inches(0.4), Inches(1.4), Inches(10.5), Inches(2.0))
    _para(
        tf, "PYTHON · DICTIONARIES", 15, YELLOW, bold=True, first=True, space_after=12
    )
    _para(tf, "Name It, Find It", 52, WHITE, bold=True, space_after=10)
    _para(tf, "Dictionaries: keys, values and instant lookup", 22, SOFT)
    tf2 = _tf(s, M + Inches(0.4), Inches(4.3), Inches(11.0), Inches(2.0))
    blue = RGBColor(0x8F, 0xB6, 0xD9)
    _para(
        tf2,
        "A list finds things by position: the 3rd item.",
        18,
        blue,
        first=True,
        space_after=8,
    )
    _para(
        tf2,
        "A dictionary finds things by name: Sara's phone — instantly.",
        18,
        blue,
    )
    tf3 = _tf(s, M + Inches(0.4), Inches(6.2), Inches(10.0), Inches(0.5))
    _para(
        tf3, "python-workbook2026  ·  dicts", 13, RGBColor(0x6E, 0x8A, 0xA3), first=True
    )


def hook_slide():
    s = slide("What is Nilu's number?", kicker="Two minutes", footer=False)
    code(
        s,
        [
            "phones = [",
            '    ("Ali", "555-01"),',
            '    ("Sara", "555-02"),',
            '    ("Nilu", "555-03"),',
            "]",
            "for name, num in phones:     # search...",
            '    if name == "Nilu":',
            "        print(num)",
        ],
        w=Inches(7.2),
    )
    tf = _tf(s, M + Inches(7.6), BODY_TOP, Inches(4.6), Inches(1.0))
    _para(tf, "With a dict: ask by name.", 19, NAVY, bold=True, first=True)
    code(
        s,
        [
            "phones = {",
            '    "Ali": "555-01",',
            '    "Sara": "555-02",',
            '    "Nilu": "555-03",',
            "}",
            'print(phones["Nilu"])',
        ],
        x=M + Inches(7.6),
        y=BODY_TOP + Inches(0.55),
        w=Inches(4.6),
        size=13,
    )
    out(s, ["555-03"], x=M + Inches(7.6), y=Inches(4.7), w=Inches(4.6))
    note(
        s,
        "Last lesson a set answered “is it here?” instantly. A dict answers "
        "*“what goes with it?”* just as fast.",
        Inches(6.0),
        kind="tip",
    )


def roadmap_slide():
    s = slide("What we cover today", kicker="Roadmap", footer=False)
    table(
        s,
        ["Part", "Topic", "You will be able to"],
        [
            ["1", "*What a dict is*", "create one, read a value, avoid KeyError"],
            ["2", "*Changing a dict*", "add, replace, delete and merge"],
            [
                "3",
                "*Looping*",
                "walk keys, values and pairs; build with a comprehension",
            ],
            ["4", "*Four patterns*", "count, group, look up, remember what you saw"],
            ["5", "*Traps*", "shared dicts, changing while looping, bad keys"],
            ["6", "*Your tasks*", "know what each exercise practises"],
        ],
        col_w=(0.8, 3.6, 7.0),
        size=16,
    )


# =================================================================== PART 1 ==
def part1():
    section(
        "What a dict is",
        "Keys pointing at values",
        ["Making a dict", "Reading: [] vs get", "Three rules"],
    )

    s = slide("A dict is a table of pairs", kicker="key → value")
    rows = [('"tea"', "5"), ('"bread"', "3"), ('"milk"', "8")]
    label(
        s,
        0.9,
        1.75,
        "keys",
        size=14,
        color=BLUE,
        bold=True,
        w=2.2,
        align=PP_ALIGN.CENTER,
    )
    label(
        s,
        4.3,
        1.75,
        "values",
        size=14,
        color=BLUE,
        bold=True,
        w=1.4,
        align=PP_ALIGN.CENTER,
    )
    for i, (k, v) in enumerate(rows):
        y = 2.2 + i * 0.95
        cell(s, 0.9, y, 2.2, 0.7, k, fill=YELLOW)
        arrow(s, 3.3, y + 0.17, 0.8)
        cell(s, 4.3, y, 1.4, 0.7, v)
    code(
        s,
        [
            'prices = {"tea": 5, "bread": 3, "milk": 8}',
            'print(prices["milk"])',
            "print(len(prices))",
        ],
        x=M + Inches(6.0),
        y=BODY_TOP,
        w=Inches(6.0),
        size=14,
    )
    out(s, ["8", "3"], x=M + Inches(6.0), y=Inches(3.2), w=Inches(6.0))
    note(
        s,
        "Each entry is a *key* and its *value*, written `key: value`. You ask with "
        "the key and get the value back — no searching.",
        Inches(5.4),
        kind="ok",
    )

    s = slide("Ways to make a dict", kicker="Syntax")
    code(
        s,
        [
            'ages = {"Ali": 19, "Sara": 21}',
            "print(ages)",
            "print(dict(Ali=19, Sara=21))",
            'print(dict([("x", 1), ("y", 2)]))',
            "print(type({}))",
        ],
        w=Inches(7.6),
    )
    out(
        s,
        [
            "{'Ali': 19, 'Sara': 21}",
            "{'Ali': 19, 'Sara': 21}",
            "{'x': 1, 'y': 2}",
            "<class 'dict'>",
        ],
        x=M + Inches(8.0),
        y=BODY_TOP,
        w=Inches(3.9),
    )
    note(
        s,
        "Remember the set trap? That's why: `{}` was given to dicts first. An empty "
        "dict is `{}` (or `dict()`); an empty set is `set()`.",
        Inches(4.3),
        kind="tip",
    )

    s = slide("Reading a missing key", kicker="[] vs get")
    code(
        s,
        [
            'ages = {"Ali": 19, "Sara": 21}',
            'print(ages.get("Bek"))',
            'print(ages.get("Bek", 0))',
            'print("Bek" in ages)',
            'ages["Bek"]',
        ],
        w=Inches(6.8),
    )
    out(
        s,
        ["None", "0", "False", "KeyError: 'Bek'"],
        x=M + Inches(7.2),
        y=BODY_TOP,
        w=Inches(4.8),
    )
    table(
        s,
        ["You write", "Key missing →"],
        [
            ['`d["k"]`', "*KeyError* — use when the key must be there"],
            ['`d.get("k")`', "`None`"],
            ['`d.get("k", 0)`', "the default you gave"],
            ['`"k" in d`', "`False` — `in` checks *keys*, not values"],
        ],
        y=Inches(4.0),
        col_w=(3.0, 8.4),
        size=15,
    )

    s = slide("Three rules of a dict", kicker="The whole idea")
    table(
        s,
        ["Rule", "So…", "Proof"],
        [
            [
                "*Keys are unique*",
                "same key twice → last one wins",
                '`{"a": 1, "a": 2}` → `{\'a\': 2}`',
            ],
            [
                "*Keys must be hashable*",
                "str, int, tuple — not list",
                "`{[1, 2]: 1}` → TypeError",
            ],
            [
                "*Insertion order kept*",
                "loops go in the order you added",
                "`list({\"z\":1, \"a\":2})` → `['z', 'a']`",
            ],
        ],
        col_w=(3.0, 3.9, 4.5),
        size=15,
    )
    code(
        s,
        ['d = {(1, 2): "pair"}     # a tuple key is fine', "print(d[(1, 2)])"],
        y=Inches(4.0),
        w=Inches(7.0),
    )
    out(s, ["pair"], x=M + Inches(7.4), y=Inches(4.0), w=Inches(4.6))
    note(
        s,
        "The *keys* of a dict behave exactly like a set (unique, hashable, instant "
        "`in`). The *values* can be anything — even lists or other dicts.",
        Inches(5.75),
        kind="ok",
    )


# =================================================================== PART 2 ==
def part2():
    section(
        "Changing a dict",
        "Add, replace, delete, merge",
        ["d[key] = value", "del and pop", "Merging with |"],
    )

    s = slide("One line adds or replaces", kicker="d[key] = value")
    code(
        s,
        [
            'ages = {"Ali": 19}',
            'ages["Sara"] = 21      # new key: added',
            'ages["Ali"] = 20       # existing key: replaced',
            "print(ages)",
            "",
            'del ages["Ali"]',
            "print(ages)",
            'print(ages.pop("Sara"))',
            "print(ages)",
            'print(ages.pop("Bek", None))',
        ],
        w=Inches(7.4),
    )
    out(
        s,
        ["{'Ali': 20, 'Sara': 21}", "{'Sara': 21}", "21", "{}", "None"],
        x=M + Inches(7.8),
        y=BODY_TOP,
        w=Inches(4.2),
    )
    note(
        s,
        "`pop` removes *and returns* the value. Give it a default (`None`) and a "
        "missing key is no longer an error.",
        Inches(6.0),
        kind="tip",
    )

    s = slide("Merging two dicts", kicker="| and update")
    code(
        s,
        [
            'a = {"x": 1, "y": 2}',
            'b = {"y": 20, "z": 30}',
            "print(a | b)      # new dict",
            "a.update(b)       # changes a",
            "print(a)",
        ],
        w=Inches(7.4),
    )
    out(
        s,
        ["{'x': 1, 'y': 20, 'z': 30}", "{'x': 1, 'y': 20, 'z': 30}"],
        x=M + Inches(7.8),
        y=BODY_TOP,
        w=Inches(4.2),
    )
    note(
        s,
        "When both have the same key, the *right-hand* side wins: `y` became 20.",
        Inches(4.3),
        kind="ok",
    )

    s = slide("The dict methods you need", kicker="Cheat sheet")
    table(
        s,
        ["Write", "Does", "If the key is missing"],
        [
            ["`d[k]`", "read the value", "*KeyError*"],
            ["`d.get(k, default)`", "read the value", "returns `default`"],
            ["`d[k] = v`", "add or replace", "adds it"],
            ["`del d[k]`", "remove", "*KeyError*"],
            ["`d.pop(k, default)`", "remove and return the value", "returns `default`"],
            ["`d.setdefault(k, v)`", "read; if missing, first store `v`", "stores `v`"],
            ["`k in d`", "is this a key?", "`False`"],
            ["`d.keys()  d.values()  d.items()`", "views for looping", "—"],
        ],
        col_w=(4.0, 4.4, 3.0),
        size=14,
    )


# =================================================================== PART 3 ==
def part3():
    section(
        "Looping",
        "Keys, values, or both",
        ["for k in d", ".values() and .items()", "Dict comprehensions", "Sorting"],
    )

    s = slide("Three ways to walk a dict", kicker="for")
    code(
        s,
        [
            'prices = {"tea": 5, "bread": 3, "milk": 8}',
            "for k in prices:          # keys",
            "    print(k)",
            "print(list(prices.values()))",
            "for name, price in prices.items():",
            '    print(f"{name}: {price}")',
        ],
        w=Inches(7.6),
    )
    out(
        s,
        ["tea", "bread", "milk", "[5, 3, 8]", "tea: 5", "bread: 3", "milk: 8"],
        x=M + Inches(8.0),
        y=BODY_TOP,
        w=Inches(3.9),
    )
    note(
        s,
        "`.items()` gives `(key, value)` tuples — unpack them straight into two "
        "names, just like `enumerate`.",
        Inches(5.9),
        kind="tip",
    )

    s = slide("Dict comprehensions", kicker="Build in one line")
    code(
        s,
        [
            "print({x: x * x for x in range(4)})",
            "",
            'code = {"A": ".-", "B": "-..."}',
            "back = {v: k for k, v in code.items()}   # flip it",
            "print(back)",
            'print(back["-..."])',
        ],
        w=Inches(8.0),
    )
    out(
        s,
        ["{0: 0, 1: 1, 2: 4, 3: 9}", "", "", "", "{'.-': 'A', '-...': 'B'}", "B"],
        x=M + Inches(8.4),
        y=BODY_TOP,
        w=Inches(3.5),
    )
    note(
        s,
        "Flipping keys and values is how `morse_decode` gets its `MORSE_TO_CHAR` "
        "table. It only works when the values are unique.",
        Inches(4.6),
        kind="ok",
    )

    s = slide("Sorting and finding the biggest", kicker="sorted, max")
    code(
        s,
        [
            'prices = {"tea": 5, "bread": 3, "milk": 8}',
            "print(sorted(prices))                # keys, A→Z",
            "print(max(prices, key=prices.get))   # key with top value",
            "print(sorted(prices.items(), key=lambda kv: kv[1]))",
        ],
        w=Inches(8.8),
    )
    out(
        s,
        ["['bread', 'milk', 'tea']", "milk", "[('bread', 3), ('tea', 5), ('milk', 8)]"],
        y=Inches(3.6),
        w=Inches(8.8),
    )
    note(
        s,
        "`max(d, key=d.get)`: loop over the keys, but compare them by their "
        "*values*. Remember it for `most_frequent_char`.",
        Inches(5.4),
        kind="tip",
    )


# =================================================================== PART 4 ==
def part4():
    section(
        "Four patterns",
        "What dicts are actually used for",
        ["Counting", "Grouping", "Lookup tables", "Remember what you saw"],
    )

    s = slide("Counting", kicker="Pattern 1 — the one you'll use most")
    code(
        s,
        [
            "counts = {}",
            'for ch in "banana":',
            "    counts[ch] = counts.get(ch, 0) + 1",
            "print(counts)",
        ],
        w=Inches(7.6),
    )
    out(s, ["{'b': 1, 'a': 3, 'n': 2}"], x=M + Inches(8.0), y=BODY_TOP, w=Inches(3.9))
    bullets(
        s,
        [
            "`get(ch, 0)`: a letter seen for the first time starts at 0",
            "One pass over the text, one instant lookup per character",
            "Two words are anagrams when their counts are equal — and `==` on dicts "
            "ignores order",
        ],
        y=Inches(3.6),
        size=18,
    )
    note(
        s,
        "Five of today's tasks start with this exact loop.",
        Inches(5.95),
        kind="ok",
    )

    s = slide("Grouping", kicker="Pattern 2")
    code(
        s,
        [
            "groups = {}",
            'for w in ["apple", "bean", "avocado", "beet", "cherry"]:',
            "    groups.setdefault(w[0], []).append(w)",
            "print(groups)",
            "print(list(groups.values()))",
        ],
        w=Inches(8.6),
    )
    out(
        s,
        [
            "{'a': ['apple', 'avocado'], 'b': ['bean', 'beet'], 'c': ['cherry']}",
            "[['apple', 'avocado'], ['bean', 'beet'], ['cherry']]",
        ],
        y=Inches(3.9),
        w=Inches(11.4),
    )
    note(
        s,
        "The key decides *which group*; the value is a list that grows. Pick a "
        "smarter key and you can group anagrams the same way.",
        Inches(5.5),
        kind="tip",
    )

    s = slide("Lookup tables", kicker="Pattern 3")
    code(
        s,
        [
            'COLORS = {"r": "red", "g": "green", "b": "blue"}',
            'print(" ".join(COLORS.get(c, "?") for c in "rgxb"))',
        ],
        w=Inches(8.8),
    )
    out(s, ["red green ? blue"], y=Inches(3.0), w=Inches(8.8))
    bullets(
        s,
        [
            "Replace a long `if / elif` chain with one dict",
            "Morse code, T9 keypads, Roman numerals, number words — all lookup tables",
            '`get(c, "")` quietly skips characters the table doesn\'t know',
        ],
        y=Inches(4.0),
        size=18,
    )

    s = slide("Remember what you saw", kicker="Pattern 4 — the seen-dict")
    code(
        s,
        [
            "nums, target = [2, 7, 11, 15], 9",
            "seen = {}                       # number -> its index",
            "for i, n in enumerate(nums):",
            "    if target - n in seen:",
            "        print([seen[target - n], i])",
            "    seen[n] = i",
        ],
        w=Inches(8.0),
    )
    out(s, ["[0, 1]"], x=M + Inches(8.4), y=BODY_TOP, w=Inches(3.5))
    note(
        s,
        "Like the seen-*set*, but it also remembers *where* (or how many, or "
        "what it mapped to). One pass instead of a loop inside a loop.",
        Inches(4.7),
        kind="ok",
    )

    s = slide("Python's ready-made helpers", kicker="Bonus")
    code(
        s,
        [
            "from collections import Counter, defaultdict",
            'c = Counter("banana")',
            "print(c)",
            "print(c.most_common(1))",
            "",
            "g = defaultdict(list)",
            'g["a"].append("apple")    # no setdefault needed',
            "print(dict(g))",
        ],
        w=Inches(7.6),
    )
    out(
        s,
        [
            "Counter({'a': 3, 'n': 2, 'b': 1})",
            "[('a', 3)]",
            "",
            "",
            "",
            "",
            "{'a': ['apple']}",
        ],
        x=M + Inches(8.0),
        y=BODY_TOP,
        w=Inches(4.0),
    )
    note(
        s,
        "Good to know — but write the plain-dict loop yourself first. Once you can, "
        "use these in real code.",
        Inches(5.6),
        kind="tip",
    )


# =================================================================== PART 5 ==
def part5():
    section(
        "Traps",
        "Three ways dicts bite",
        ["Two names, one dict", "Changing while looping", "Lists as keys"],
    )

    s = slide("Two names, one dict", kicker="Names are arrows")
    code(
        s,
        [
            'a = {"x": 1}',
            "b = a              # not a copy!",
            'b["y"] = 2',
            "print(a)",
            "",
            "c = a.copy()       # a real copy",
            'c["z"] = 3',
            "print(a)",
        ],
        w=Inches(7.0),
    )
    out(
        s,
        ["{'x': 1, 'y': 2}", "{'x': 1, 'y': 2}"],
        x=M + Inches(7.4),
        y=BODY_TOP,
        w=Inches(4.6),
    )
    note(
        s,
        "Same as lists: `=` copies the arrow, not the dict. Use `.copy()` or "
        "`dict(a)` when you need your own.",
        Inches(5.6),
        kind="warn",
    )

    s = slide("Don't change a dict while looping over it", kicker="Trap")
    code(
        s,
        [
            'd = {"a": 1, "b": 0, "c": 2}',
            "for k in d:",
            "    if d[k] == 0:",
            "        del d[k]",
        ],
        w=Inches(6.4),
    )
    out(
        s,
        ["RuntimeError: dictionary changed", "size during iteration"],
        x=M + Inches(6.8),
        y=BODY_TOP,
        w=Inches(5.2),
        label="What you get",
    )
    code(
        s,
        ["d = {k: v for k, v in d.items() if v != 0}   # build a new one", "print(d)"],
        y=Inches(3.6),
        w=Inches(9.0),
    )
    out(s, ["{'a': 1, 'c': 2}"], y=Inches(4.8), w=Inches(9.0))
    note(
        s,
        "Changing *values* while looping is fine. Adding or removing *keys* is not "
        "— build a new dict, or loop over `list(d)`.",
        Inches(6.0),
        kind="warn",
    )

    s = slide("Keys must not change", kicker="Hashable")
    code(s, ['d = {[1, 2]: "x"}'], w=Inches(5.0))
    out(
        s,
        ["TypeError: unhashable type: 'list'"],
        x=M + Inches(5.4),
        y=BODY_TOP,
        w=Inches(6.5),
        label="What you get",
    )
    bullets(
        s,
        [
            "A key's place is computed from it when it goes in — exactly like a set",
            "So keys must never change: str, int, tuple, frozenset",
            "Need a list as a key? Turn it into a tuple: `tuple(sorted(word))`",
            "Values have no such rule — store lists, sets, even other dicts",
        ],
        y=Inches(3.0),
        size=18,
        gap=10,
    )
    note(
        s,
        '`tuple(sorted(word))` — or `"".join(sorted(word))` — is a perfect key for '
        "`group_anagrams`. Why? Try it on “eat” and “tea”.",
        Inches(5.7),
        kind="tip",
    )


# =================================================================== PART 6 ==
def part6():
    section(
        "Your tasks",
        "Fourteen exercises in dicts/",
        ["Counting", "Lookup tables", "Comparing and remembering", "How to check"],
    )

    s = slide("Counting and lookup tables", kicker="dicts/ — start here")
    table(
        s,
        ["Exercise", "Level", "What it practises"],
        [
            ["`chars_count`", "start here", "the counting loop, returned as a dict"],
            [
                "`most_frequent_char`",
                "easy",
                "count, then `max(..., key=...)`; empty → ValueError",
            ],
            ["`first_unique_char`", "easy", "count first, then a second pass in order"],
            ["`read_aloud`", "medium", "three lookup tables: ONES, TEENS, TENS"],
            ["`morse_encode`", "medium", "table lookup, skip unknown characters"],
            ["`morse_decode`", "medium", "the flipped table `MORSE_TO_CHAR`"],
            [
                "`roman_to_int`",
                "medium",
                "lookup + “smaller before bigger means minus”",
            ],
            ["`text_messaging`", "medium", "the T9 keypad as a dict"],
        ],
        col_w=(3.6, 1.6, 6.2),
        size=14,
    )

    s = slide("Comparing and remembering", kicker="dicts/ — then these")
    table(
        s,
        ["Exercise", "Level", "What it practises"],
        [
            ["`is_anagram`", "easy", "two counts, one `==`"],
            ["`is_phrase_anagram`", "medium", "the same, ignoring spaces and case"],
            [
                "`group_anagrams`",
                "medium",
                "grouping with a sorted-letters key — hint inside",
            ],
            ["`two_sum`", "medium", "the seen-dict: number → index — hint inside"],
            [
                "`isomorphic_strings`",
                "medium",
                "a mapping that must work in *both* directions",
            ],
            [
                "`longest_substring_without_repeating`",
                "hard",
                "last-seen index of each char + a sliding window — hint inside",
            ],
        ],
        col_w=(4.6, 1.4, 5.4),
        size=14,
    )
    note(
        s,
        "Read `dicts/_docs/` first — dict_basics, then dict_operations, then "
        "dict_best_practices.",
        Inches(5.4),
        kind="tip",
    )

    s = slide("Checking your work", kicker="Same as always")
    code(
        s,
        [
            "uv run pytest dicts/two_sum/      # one exercise",
            "uv run pytest dicts/              # the whole topic",
        ],
        w=Inches(9.0),
    )
    bullets(
        s,
        [
            "Create `dicts/two_sum/two_sum.py` next to the statement — name matches "
            "the folder",
            "Morse, T9, Roman, read_aloud: copy the table from the statement into "
            "your file",
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
    _para(
        tf, "Reach for a dict when…", 42, WHITE, bold=True, first=True, space_after=22
    )
    soft = RGBColor(0xC3, 0xD3, 0xE1)
    for line in [
        "…you look things up by name, not by position.",
        "…you count, group, or translate one thing into another.",
        "…you need to remember what you've seen — and where.",
    ]:
        _para(tf, line, 22, soft, space_after=14)
    tf2 = _tf(s, Inches(1.3), Inches(5.4), Inches(10.7), Inches(1.0))
    _para(
        tf2,
        "counts[x] = counts.get(x, 0) + 1 — you'll write it a hundred times.",
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
