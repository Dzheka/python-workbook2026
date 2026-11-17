"""Build the "Names Are Arrows" deck — pointers, lists and tuples in memory.

A third deck on lists. The tuples deck says *what* happens when two names
share a list; this one draws *why*: a name is an arrow to an object, a list is
a row of arrows, and a growing list quietly moves its row of arrows to a bigger
block of memory. Tuples come back at the end as the row of arrows that never
grows, which explains why `+=` behaves differently on the two.

Every output on these slides was produced by running the code on CPython 3.13.
Sizes from `sys.getsizeof` are CPython 3.13 on a 64-bit machine; other versions
print other numbers, but the pattern is the same.

Run:  uv run --with python-pptx python slides/lists/build_memory_deck.py
"""

from pathlib import Path

from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Pt

from _deck import (
    BLUE,
    BODY_TOP,
    GRAY,
    GREEN,
    LIGHT,
    M,
    MONO,
    NAVY,
    RED,
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

OUT = Path(__file__).with_name("memory.pptx")

BORDER = RGBColor(0xB4, 0xC5, 0xD6)
FADED = RGBColor(0xC9, 0xD2, 0xDB)
PALE = RGBColor(0xFA, 0xFB, 0xFC)


# ---------------------------------------------------------- diagram parts --
def _i(v):
    return Inches(v)


def label(s, x, y, text, size=12, color=GRAY, w=3.0, align=PP_ALIGN.LEFT, bold=False):
    tf = _tf(s, _i(x), _i(y), _i(w), _i(0.35))
    _para(tf, text, size, color, first=True, align=align, bold=bold)


def name(s, x, y, text, w=0.9, faded=False):
    """A variable name: a yellow tag. Returns the point an arrow leaves from."""
    h = 0.5
    shp = _box(
        s,
        _i(x),
        _i(y),
        _i(w),
        _i(h),
        fill=PALE if faded else YELLOW,
        line=FADED if faded else None,
        shape=MSO_SHAPE.ROUNDED_RECTANGLE,
        radius=0.2,
    )
    tf = shp.text_frame
    tf.margin_left = tf.margin_right = 0
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    _para(tf, text, 17, FADED if faded else NAVY, bold=True, font=MONO, first=True,
          align=PP_ALIGN.CENTER)
    return (x + w, y + h / 2)


def obj(s, x, y, text, w=1.2, h=0.62, kind=None, faded=False, size=17):
    """An object in memory: a light box with its type in small caps above."""
    shp = _box(
        s,
        _i(x),
        _i(y),
        _i(w),
        _i(h),
        fill=PALE if faded else LIGHT,
        line=FADED if faded else BLUE,
        shape=MSO_SHAPE.ROUNDED_RECTANGLE,
        radius=0.12,
    )
    tf = shp.text_frame
    tf.margin_left = tf.margin_right = 0
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    _para(tf, text, size, FADED if faded else NAVY, bold=True, font=MONO, first=True,
          align=PP_ALIGN.CENTER)
    if kind:
        label(s, x, y - 0.3, kind, size=10, color=FADED if faded else GRAY, w=w + 1,
              bold=True)
    return shp


def arrow(s, x1, y1, x2, y2, color=BLUE, width=2.0, dashed=False):
    c = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, _i(x1), _i(y1), _i(x2), _i(y2))
    c.line.color.rgb = color
    c.line.width = Pt(width)
    ln = c.line._get_or_add_ln()
    if dashed:
        dash = ln.makeelement(qn("a:prstDash"), {"val": "dash"})
        ln.append(dash)
    tail = ln.makeelement(qn("a:tailEnd"), {"type": "triangle", "w": "med", "len": "med"})
    ln.append(tail)
    return c


def slots(s, x, y, n, cell=0.62, h=0.62, used=None, faded=False, header=None):
    """A row of pointer cells. Returns the centre point of each cell.

    used: how many cells hold an arrow; the rest are drawn empty (spare
    capacity). header: optional text drawn in a box left of the cells.
    """
    used = n if used is None else used
    line = FADED if faded else BLUE
    cx = x
    if header:
        hw = 1.0
        hb = _box(s, _i(x), _i(y), _i(hw), _i(h), fill=NAVY if not faded else PALE,
                  line=None if not faded else FADED)
        tf = hb.text_frame
        tf.margin_left = tf.margin_right = 0
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        _para(tf, header, 12, WHITE if not faded else FADED, bold=True, font=MONO,
              first=True, align=PP_ALIGN.CENTER)
        cx = x + hw
    centres = []
    for i in range(n):
        filled = i < used
        _box(s, _i(cx + i * cell), _i(y), _i(cell), _i(h),
             fill=(PALE if faded else WHITE) if filled else PALE, line=line)
        c = (cx + i * cell + cell / 2, y + h / 2)
        if filled:
            _box(s, _i(c[0] - 0.06), _i(c[1] - 0.06), _i(0.12), _i(0.12),
                 fill=FADED if faded else BLUE, shape=MSO_SHAPE.OVAL)
        else:
            label(s, cx + i * cell, y + h / 2 - 0.15, "·", size=14, color=FADED,
                  w=cell, align=PP_ALIGN.CENTER)
        centres.append(c)
    return centres


def framed(s, x, y, w, h, title=None):
    """A soft frame grouping one diagram; optional title above it."""
    _box(s, _i(x), _i(y), _i(w), _i(h), fill=None, line=RGBColor(0xDD, 0xE4, 0xEA),
         shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.04)
    if title:
        label(s, x + 0.15, y + 0.12, title, size=12, color=BLUE, w=w - 0.3, bold=True)


# ================================================================== TITLE ==
def title_slide():
    s = prs.slides.add_slide(prs.slide_layouts[6])
    _box(s, 0, 0, W, H, fill=NAVY)
    _box(s, 0, H - Inches(0.28), W, Inches(0.28), fill=YELLOW)
    _box(s, M, Inches(1.5), Inches(0.12), Inches(1.5), fill=YELLOW)
    tf = _tf(s, M + Inches(0.4), Inches(1.4), Inches(10.5), Inches(2.0))
    _para(tf, "PYTHON · LISTS, PART 3", 15, YELLOW, bold=True, first=True,
          space_after=12)
    _para(tf, "Names Are Arrows", 52, WHITE, bold=True, space_after=10)
    _para(tf, "Pointers, lists and tuples in memory", 22, RGBColor(0xA9, 0xBD, 0xD1))
    tf2 = _tf(s, M + Inches(0.4), Inches(4.3), Inches(11.0), Inches(2.0))
    _para(tf2, "Last time: two names can share one list.", 18,
          RGBColor(0x8F, 0xB6, 0xD9), first=True, space_after=8)
    _para(tf2, "Today: we draw the memory and watch it happen.", 18,
          RGBColor(0x8F, 0xB6, 0xD9))
    tf3 = _tf(s, M + Inches(0.4), Inches(6.2), Inches(10.0), Inches(0.5))
    _para(tf3, "python-workbook2026  ·  lists", 13, RGBColor(0x6E, 0x8A, 0xA3),
          first=True)


def hook_slide():
    s = slide("Same line, different result", kicker="Two minutes", footer=False)
    code(s, ["p = [1, 2, 3]", "q = p", "p += [4]", "print(q)"],
         w=Inches(5.6), caption="with a list")
    code(s, ["x = (1, 2, 3)", "y = x", "x += (4,)", "print(y)"],
         x=M + Inches(6.3), w=Inches(5.6), caption="with a tuple")
    out(s, ["[1, 2, 3, 4]"], y=Inches(4.15), w=Inches(5.6), label="q")
    out(s, ["(1, 2, 3)"], x=M + Inches(6.3), y=Inches(4.15), w=Inches(5.6),
        label="y")
    note(s, "The code is identical. One name changed, the other did not. By the "
         "end of today you will be able to *draw* why.", Inches(5.8), kind="tip")


def roadmap_slide():
    s = slide("What we cover today", kicker="Roadmap", footer=False)
    table(
        s,
        ["Part", "Topic", "You will be able to"],
        [
            ["1", "*Names are arrows*", "draw what `=` really does"],
            ["2", "*A list is a row of arrows*", "draw a list, and a list of lists"],
            ["3", "*How a list grows*", "explain what happens in memory on `append`"],
            ["4", "*Tuples in memory*", "explain why a tuple never grows"],
            ["5", "*Check yourself*", "predict the output before you run it"],
        ],
        col_w=(0.8, 4.0, 6.6),
        size=16,
    )
    note(s, "One picture for the whole lesson: *a name is an arrow, an object is "
         "a box.* `=` moves an arrow. A method changes a box.", Inches(5.2),
         kind="ok")


# =================================================================== PART 1 ==
def part1():
    section("Names are arrows", "What a variable really is",
            ["Name → object", "Two names, one object", "Moving vs changing"])

    s = slide("A variable is an arrow, not a box", kicker="Pointers")
    code(s, ["x = 10"], w=Inches(4.6))
    framed(s, 6.0, 1.75, 6.6, 2.6, title="MEMORY")
    px, py = name(s, 6.5, 2.75, "x")
    obj(s, 9.6, 2.69, "10", kind="INT")
    arrow(s, px, py, 9.6, py)
    bullets(s, [
        "Python makes the object `10` somewhere in memory",
        "The name `x` just *points* at it — it holds the address",
        "`id(x)` shows that address as a number",
    ], y=Inches(3.0), w=Inches(5.0), size=17)
    note(s, "In other languages a variable is a box you put a value in. In Python "
         "it is a label tied to an object. That label is what we call a *pointer*.",
         Inches(5.6), kind="ok")

    s = slide("Two names, one object", kicker="y = x")
    code(s, ["x = 10", "y = x          # copy the ARROW", "x = x + 1      # new object",
             "print(x, y)"], w=Inches(5.0))
    out(s, ["11 10"], y=Inches(3.7), w=Inches(5.0))
    framed(s, 6.2, 1.75, 6.4, 2.0, title="AFTER  y = x")
    nx = name(s, 6.6, 2.25, "x")
    ny = name(s, 6.6, 3.0, "y")
    obj(s, 9.8, 2.6, "10")
    arrow(s, nx[0], nx[1], 9.8, 2.85)
    arrow(s, ny[0], ny[1], 9.8, 3.0)
    framed(s, 6.2, 3.95, 6.4, 2.0, title="AFTER  x = x + 1")
    nx = name(s, 6.6, 4.45, "x")
    ny = name(s, 6.6, 5.2, "y")
    obj(s, 9.8, 4.39, "11")
    obj(s, 9.8, 5.14, "10")
    arrow(s, nx[0], nx[1], 9.8, nx[1], color=GREEN)
    arrow(s, ny[0], ny[1], 9.8, ny[1])
    note(s, "`x + 1` builds a *new* object and `=` swings x's arrow to it. y still "
         "points at the old 10.", Inches(6.15), kind="tip")

    s = slide("Moving an arrow vs changing a box", kicker="The key distinction")
    table(
        s,
        ["You write", "What happens in memory", "Others who share it see it?"],
        [
            ["`a = something`", "the arrow `a` moves to another object", "no"],
            ["`a = a + [4]`", "a *new* list is built, `a` moves to it", "no"],
            ["`a.append(4)`", "the box `a` points at is changed", "*yes*"],
            ["`a[0] = 9`", "one slot inside the box now points elsewhere", "*yes*"],
            ["`a += [4]`  (list)", "the box is changed, `a` stays put", "*yes*"],
        ],
        col_w=(2.6, 5.6, 3.2),
        size=15,
    )
    note(s, "Only changing a box can surprise another name. Moving an arrow "
         "never does.", Inches(5.4), kind="ok")


# =================================================================== PART 2 ==
def part2():
    section("A list is a row of arrows", "It does not hold your values",
            ["Slots hold addresses", "One list, three times", "What getsizeof counts"])

    s = slide("A list stores arrows, not values", kicker="Inside a list")
    code(s, ["nums = [10, 20, 30]"], w=Inches(4.6))
    framed(s, 0.7, 2.75, 11.9, 2.9)
    pn = name(s, 1.1, 3.2, "nums", w=1.1)
    cs = slots(s, 3.4, 3.2, 3, header="len 3")
    arrow(s, pn[0], pn[1], 3.4, pn[1])
    label(s, 3.4, 2.85, "LIST OBJECT", size=10, bold=True)
    for (cx, cy), v, ox in zip(cs, ["10", "20", "30"], [3.9, 5.4, 6.9]):
        obj(s, ox, 4.6, v, w=1.1, kind="INT")
        arrow(s, cx, cy + 0.06, ox + 0.55, 4.6)
    tf = _tf(s, Inches(8.6), Inches(3.15), Inches(3.8), Inches(2.3))
    _para(tf, "Each slot is 8 bytes:", 16, NAVY, bold=True, first=True, space_after=4)
    _para(tf, "just the address of an object that lives somewhere else.", 15, GRAY,
          space_after=10)
    _para(tf, "That is why a list can mix types — every slot is the same size.",
          15, GRAY)
    note(s, "`nums[1]` means: go to slot 1, follow its arrow. `nums[1] = 99` means: "
         "make slot 1 point at `99` instead.", Inches(5.95), kind="ok")

    s = slide("One list, three times", kicker="[[0] * 3] * 3")
    code(s, ["grid = [[0] * 3] * 3", "grid[0][0] = 1", "print(grid)"], w=Inches(5.6))
    out(s, ["[[1, 0, 0], [1, 0, 0], [1, 0, 0]]"], y=Inches(3.15), w=Inches(5.6))
    framed(s, 6.7, 1.75, 5.9, 3.7, title="MEMORY")
    pg = name(s, 6.95, 2.4, "grid", w=1.0)
    outer = slots(s, 8.5, 2.4, 3, cell=0.55, h=0.5)
    arrow(s, pg[0], pg[1], 8.5, pg[1])
    inner = slots(s, 8.5, 4.4, 3, cell=0.55, h=0.5, used=0)
    for i, (cx, cy) in enumerate(outer):
        arrow(s, cx, cy + 0.06, 8.5 + 0.825, 4.4, color=RED)
    label(s, 8.5, 4.95, "the only inner list", size=11, color=RED, w=2.5)
    code(s, ["grid = [[0] * 3 for _ in range(3)]   # three separate rows"],
         y=Inches(4.6), w=Inches(5.6), size=13)
    note(s, "`* 3` copies the *arrows* in the outer list, not the inner list. All "
         "three rows are the same row.", Inches(5.95), kind="warn")

    s = slide("A list's size counts arrows only", kicker="sys.getsizeof")
    code(s, [
        "import sys",
        "",
        'small = ["a"]',
        'huge = ["a" * 1000]',
        "",
        "print(sys.getsizeof(small))",
        "print(sys.getsizeof(huge))",
        'print(sys.getsizeof("a" * 1000))',
    ], w=Inches(6.4))
    out(s, ["64", "64", "1041"], x=M + Inches(6.8), y=BODY_TOP, w=Inches(5.0))
    tf = _tf(s, M + Inches(6.8), BODY_TOP + Inches(1.6), Inches(5.0), Inches(2.0))
    _para(tf, "Same size list.", 18, NAVY, bold=True, first=True, space_after=6)
    _para(tf, "Both lists hold one arrow. The 1000-letter string lives outside the "
          "list, and `getsizeof` does not follow arrows.", 16, GRAY)
    note(s, "A list is a small header plus 8 bytes per slot. That number is about "
         "to start doing something strange.", Inches(5.6), kind="tip")


# =================================================================== PART 3 ==
def part3():
    section("How a list grows", "What memory does on every append",
            ["Spare seats", "Moving to a bigger block", "append vs + vs +="])

    s = slide("A list keeps spare seats", kicker="Over-allocation")
    code(s, [
        "import sys",
        "",
        "a = []",
        "for i in range(18):",
        "    print(len(a), sys.getsizeof(a))",
        "    a.append(i)",
    ], w=Inches(5.6))
    table(
        s,
        ["len", "bytes", "slots reserved"],
        [
            ["0", "56", "0"],
            ["1 – 4", "88", "4"],
            ["5 – 8", "120", "8"],
            ["9 – 16", "184", "16"],
            ["17", "248", "24"],
        ],
        x=M + Inches(6.0),
        w=Inches(5.9),
        col_w=(1.4, 1.4, 2.4),
        size=16,
    )
    label(s, 6.7, 4.25, "bytes = 56 header + 8 × slots   (CPython 3.13)", size=12,
          w=5.9)
    note(s, "The size does not grow by 8 on every append. Python reserves *more "
         "slots than it needs*, then fills them up for free until they run out.",
         Inches(5.6), kind="ok")

    s = slide("When the seats run out, the row moves", kicker="Memory refresh")
    label(s, 0.7, 1.7, "1.  a has 4 items and 4 slots — full", size=15, color=NAVY,
          w=8, bold=True)
    pa = name(s, 0.9, 2.2, "a")
    slots(s, 2.5, 2.2, 0, header="list")
    arrow(s, pa[0], pa[1], 2.5, pa[1])
    old = slots(s, 5.0, 2.2, 4, faded=False)
    arrow(s, 3.5, 2.51, 5.0, 2.51)
    label(s, 5.0, 2.85, "old block", size=11, w=2.5)

    label(s, 0.7, 3.4, "2.  a.append(5): Python asks for a bigger block and copies "
          "the 4 arrows over", size=15, color=NAVY, w=11.5, bold=True)
    pa = name(s, 0.9, 3.9, "a")
    slots(s, 2.5, 3.9, 0, header="list")
    arrow(s, pa[0], pa[1], 2.5, pa[1])
    slots(s, 5.0, 3.9, 4, faded=True)
    label(s, 5.0, 4.55, "old block — freed", size=11, color=FADED, w=2.5)
    slots(s, 8.0, 3.9, 8, cell=0.55, used=5)
    arrow(s, 3.5, 4.21, 4.95, 4.21, color=FADED, dashed=True)
    arrow(s, 7.5, 4.21, 8.0, 4.21, color=GREEN)
    label(s, 8.0, 4.55, "new block: 4 copied + 1 new + 3 spare", size=11,
          color=GREEN, w=4.5)
    tf = _tf(s, Inches(0.7), Inches(5.0), Inches(11.9), Inches(0.5))
    _para(tf, "The list header (and its id) never moves. Only the row of arrows "
          "behind it does — the values themselves are not copied.", 15, GRAY,
          first=True)
    note(s, "This is why `id(a)` is the same before and after `append`: the box "
         "`a` points at is the same box, it just got a bigger back room.",
         Inches(5.85), kind="ok")

    s = slide("append, +=, and + are not the same", kicker="Proof with id()")
    code(s, [
        "a = [1, 2, 3]",
        "",
        "before = id(a);  a.append(4)",
        "print(id(a) == before)",
        "",
        "before = id(a);  a += [5]",
        "print(id(a) == before)",
        "",
        "before = id(a);  a = a + [6]",
        "print(id(a) == before)",
    ], w=Inches(6.6))
    out(s, ["True", "True", "False"], x=M + Inches(7.0), y=BODY_TOP, w=Inches(5.0))
    tf = _tf(s, M + Inches(7.0), BODY_TOP + Inches(1.65), Inches(5.0), Inches(2.4))
    _para(tf, "append and += change the box.", 17, NAVY, bold=True, first=True,
          space_after=8)
    _para(tf, "a + [6] builds a whole new list and moves the arrow — every "
          "item's arrow is copied into it.", 16, GRAY)
    note(s, "On a list, `a += b` is `a.extend(b)`. It is *not* shorthand for "
         "`a = a + b`. That is half of the answer to slide 2.", Inches(6.0),
         kind="warn")

    s = slide("Why the refresh matters to you", kicker="Speed")
    table(
        s,
        ["Operation", "What memory does", "Cost"],
        [
            ["`a.append(x)`", "fill a spare slot; move the row only now and then",
             "*cheap*"],
            ["`a.pop()`", "empty the last slot", "*cheap*"],
            ["`a.insert(0, x)`", "shift every arrow one slot right", "grows with len"],
            ["`a.pop(0)`", "shift every arrow one slot left", "grows with len"],
            ["`a = a + [x]`  in a loop", "copy the whole row every time",
             "grows with len"],
        ],
        col_w=(3.2, 6.0, 2.2),
        size=15,
    )
    note(s, "Build lists with `append` and add to the *end*. Moving the row is "
         "rare enough that append stays fast on average.", Inches(5.3), kind="tip")


# =================================================================== PART 4 ==
def part4():
    section("Tuples in memory", "The row of arrows that never grows",
            ["No spare seats", "+= builds a new tuple", "Solving slide 2",
             "A fixed arrow to a list"])

    s = slide("A tuple is a fixed row of arrows", kicker="No spare seats")
    framed(s, 0.7, 1.75, 5.8, 2.5, title="t = (1, 2, 3)")
    pt = name(s, 1.0, 2.45, "t")
    slots(s, 2.4, 2.45, 3, header="len 3")
    arrow(s, pt[0], pt[1], 2.4, pt[1])
    label(s, 2.4, 3.2, "exactly 3 slots, stored with the header", size=12, w=4)
    framed(s, 6.8, 1.75, 5.8, 2.5, title="a = [1, 2, 3]")
    pl = name(s, 7.1, 2.45, "a")
    slots(s, 8.5, 2.45, 0, header="list")
    arrow(s, pl[0], pl[1], 8.5, pl[1])
    slots(s, 9.9, 2.45, 4, cell=0.55, used=3)
    arrow(s, 9.5, 2.76, 9.9, 2.76)
    label(s, 8.5, 3.2, "header + separate row with a spare slot", size=12, w=4)
    code(s, [
        "print(sys.getsizeof(()),  sys.getsizeof([]))",
        "print(sys.getsizeof((1, 2, 3)),  sys.getsizeof([1, 2, 3]))",
    ], y=Inches(4.45), w=Inches(7.6), size=14)
    out(s, ["40 56", "64 88"], x=M + Inches(8.0), y=Inches(4.45), w=Inches(3.9))
    note(s, "A tuple can never grow, so it never needs spare seats or a row it "
         "can move. Smaller, and one less arrow to follow.", Inches(6.0), kind="ok")

    s = slide("Changing a tuple means building a new one", kicker="tuple +=")
    code(s, ["x = (1, 2, 3)", "y = x", "", "before = id(x)", "x += (4,)",
             "print(id(x) == before)", "print(x, y)"], w=Inches(5.4))
    out(s, ["False", "(1, 2, 3, 4) (1, 2, 3)"], y=Inches(4.45), w=Inches(5.4))
    framed(s, 6.5, 1.75, 6.1, 3.9, title="AFTER  x += (4,)")
    py_ = name(s, 6.8, 2.6, "y")
    slots(s, 8.4, 2.6, 3, header="len 3")
    arrow(s, py_[0], py_[1], 8.4, py_[1])
    label(s, 8.4, 3.25, "old tuple — untouched", size=11, w=3.5)
    px_ = name(s, 6.8, 4.1, "x")
    slots(s, 8.4, 4.1, 4, cell=0.55, header="len 4")
    arrow(s, px_[0], px_[1], 8.4, px_[1], color=GREEN)
    label(s, 8.4, 4.75, "new tuple — 3 arrows copied + 1", size=11, color=GREEN,
          w=3.8)
    note(s, "A tuple has no room to grow and no permission to change, so `+=` "
         "has only one option: build a new tuple and move the arrow.",
         Inches(6.0), kind="ok")

    s = slide("Slide 2, solved", kicker="Draw it")
    framed(s, 0.7, 1.75, 5.8, 3.4, title="p += [4]   — list")
    pp = name(s, 1.0, 2.5, "p")
    pq = name(s, 1.0, 3.6, "q")
    slots(s, 2.9, 3.0, 4, cell=0.55, header="list")
    arrow(s, pp[0], pp[1], 2.9, 3.2)
    arrow(s, pq[0], pq[1], 2.9, 3.4)
    label(s, 2.9, 3.7, "one box, grown in place", size=12, color=GREEN, w=3.5)
    framed(s, 6.8, 1.75, 5.8, 3.4, title="x += (4,)   — tuple")
    pxx = name(s, 7.1, 2.5, "x")
    pyy = name(s, 7.1, 3.8, "y")
    slots(s, 8.6, 2.5, 4, cell=0.5, header="len 4")
    slots(s, 8.6, 3.8, 3, cell=0.5, header="len 3")
    arrow(s, pxx[0], pxx[1], 8.6, pxx[1], color=GREEN)
    arrow(s, pyy[0], pyy[1], 8.6, pyy[1])
    label(s, 8.6, 4.4, "two boxes — y kept the old one", size=12, color=GREEN, w=3.8)
    bullets(s, [
        "Same symbol `+=`, two different jobs",
        "List: *change the box* — every name on it sees the change",
        "Tuple: *build a new box, move one arrow* — nobody else is affected",
    ], y=Inches(5.3), size=17, gap=5)

    s = slide("A tuple's arrows are fixed — not their targets",
              kicker="Tuple holding a list")
    code(s, ["t = (1, [2, 3])", "t[1].append(4)", "print(t)"], w=Inches(5.2))
    out(s, ["(1, [2, 3, 4])"], y=Inches(3.15), w=Inches(5.2))
    framed(s, 6.3, 1.75, 6.3, 3.6, title="MEMORY")
    pt = name(s, 6.55, 2.45, "t")
    cs = slots(s, 7.8, 2.45, 2, header="tuple")
    arrow(s, pt[0], pt[1], 7.8, pt[1])
    obj(s, 8.5, 4.2, "1", w=0.9, kind="INT")
    arrow(s, cs[0][0], cs[0][1] + 0.06, 8.95, 4.2)
    slots(s, 10.2, 4.2, 3, cell=0.5, h=0.55, used=3)
    label(s, 10.2, 3.9, "LIST — can grow", size=10, color=GRAY, bold=True, w=2.3)
    arrow(s, cs[1][0], cs[1][1] + 0.06, 10.6, 4.2, color=RED)
    label(s, 10.2, 4.8, "+ 1 new slot", size=11, color=GREEN, w=2.3)
    note(s, "Slot 1 of the tuple still points at the *same* list — that arrow can "
         "never move. The list at the end of it is free to change.", Inches(5.6),
         kind="warn")


# =================================================================== PART 5 ==
def part5():
    section("Check yourself", "Predict, then draw, then run",
            ["Three short programs", "Answers with pictures"])

    s = slide("What does each one print?", kicker="Predict first")
    code(s, ["a = [1, 2]", "b = a", "a = a + [3]", "print(b)"],
         w=Inches(3.7), caption="1")
    code(s, ["t = ([],)", "t[0].append(1)", "print(t)"],
         x=M + Inches(4.1), w=Inches(3.7), caption="2")
    code(s, ["rows = [[]] * 2", 'rows[0].append("x")', "print(rows)"],
         x=M + Inches(8.2), w=Inches(3.7), caption="3")
    note(s, "Draw the arrows on paper before you answer. Every one of these has "
         "an obvious answer that is wrong.", Inches(5.0), kind="tip")

    s = slide("Answers", kicker="Check yourself")
    table(
        s,
        ["#", "Output", "Why — in arrows"],
        [
            ["1", "`[1, 2]`",
             "`a + [3]` built a new list and moved `a`; `b` kept the old one"],
            ["2", "`([1],)`",
             "the tuple's slot still points at the same list; that list grew"],
            ["3", "`[['x'], ['x']]`",
             "`* 2` copied one arrow twice — both rows are the same list"],
        ],
        col_w=(0.6, 2.6, 8.2),
        size=16,
    )
    note(s, "If you got all three, you can read memory. If not, redraw the one "
         "you missed — the picture always gives the right answer.", Inches(4.2),
         kind="ok")


# ================================================================= CLOSING ==
def closing():
    s = prs.slides.add_slide(prs.slide_layouts[6])
    _box(s, 0, 0, W, H, fill=NAVY)
    _box(s, 0, H - Inches(0.28), W, Inches(0.28), fill=YELLOW)
    tf = _tf(s, Inches(1.3), Inches(1.2), Inches(10.7), Inches(4.2))
    _para(tf, "Three sentences", 42, WHITE, bold=True, first=True, space_after=22)
    soft = RGBColor(0xC3, 0xD3, 0xE1)
    for head, rest in [
        ("A name is an arrow.", "  = moves it; nothing else does."),
        ("A list is a row of arrows", " with spare seats, and moves the row when "
         "they run out."),
        ("A tuple is a row of arrows that never changes", " — so changing it "
         "means building a new one."),
    ]:
        p = _para(tf, head, 22, YELLOW, bold=True, space_after=14)
        r = p.add_run()
        r.text = rest
        r.font.size = Pt(20)
        r.font.name = "Trebuchet MS"
        r.font.color.rgb = soft
    tf2 = _tf(s, Inches(1.3), Inches(5.5), Inches(10.7), Inches(1.0))
    _para(tf2, "When in doubt: draw the arrows.", 20, YELLOW, bold=True, first=True)


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
