"""Build the "Doing It Again" PowerPoint deck for the repetitions topic.

Starts from work a person would never do by hand, then walks the material in
``repetitions/_docs``: the `for` loop and `range`, the `while` loop, `break`
and `continue`, accumulator patterns, and nested loops.

The drawing primitives are the same ones used by the intro and conditionals
decks, so all three look like one course.

Run:  uv run --with python-pptx python slides/repetitions/build_repetitions_deck.py
"""

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Emu, Inches, Pt

OUT = Path(__file__).with_name("repetitions.pptx")

# ---------------------------------------------------------------- palette --
NAVY = RGBColor(0x1E, 0x2A, 0x38)
BLUE = RGBColor(0x37, 0x76, 0xAB)
YELLOW = RGBColor(0xFF, 0xD4, 0x3B)
GRAY = RGBColor(0x5A, 0x66, 0x72)
LIGHT = RGBColor(0xF2, 0xF5, 0xF8)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
CODE_FG = RGBColor(0xE8, 0xEE, 0xF4)
GREEN = RGBColor(0x2E, 0x7D, 0x32)
RED = RGBColor(0xC6, 0x28, 0x28)

SANS = "Trebuchet MS"
MONO = "Consolas"

W, H = Inches(13.333), Inches(7.5)
M = Inches(0.7)  # left/right margin
BODY_TOP = Inches(1.75)
BODY_W = W - 2 * M

prs = Presentation()
prs.slide_width, prs.slide_height = W, H
BLANK = prs.slide_layouts[6]

_section = {"n": 0, "name": ""}


# ------------------------------------------------------------- primitives --
def _box(
    slide, x, y, w, h, fill=None, line=None, shape=MSO_SHAPE.RECTANGLE, radius=None
):
    s = slide.shapes.add_shape(shape, x, y, w, h)
    if fill is None:
        s.fill.background()
    else:
        s.fill.solid()
        s.fill.fore_color.rgb = fill
    if line is None:
        s.line.fill.background()
    else:
        s.line.color.rgb = line
        s.line.width = Pt(1.25)
    s.shadow.inherit = False
    if radius is not None and shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        s.adjustments[0] = radius
    return s


def _tf(slide, x, y, w, h, anchor=MSO_ANCHOR.TOP):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Inches(0.06)
    tf.margin_top = tf.margin_bottom = 0
    return tf


def _para(
    tf,
    text,
    size,
    color,
    bold=False,
    font=SANS,
    first=False,
    space_before=0,
    space_after=0,
    align=PP_ALIGN.LEFT,
    italic=False,
):
    p = tf.paragraphs[0] if first else tf.add_paragraph()
    p.alignment = align
    p.space_before = Pt(space_before)
    p.space_after = Pt(space_after)
    if text:
        r = p.add_run()
        r.text = text
        f = r.font
        f.size, f.bold, f.italic, f.name = Pt(size), bold, italic, font
        f.color.rgb = color
    return p


def _rich(p, parts, size, default_color, font=SANS):
    """parts: list of (text, color|None, bold, mono)."""
    for text, color, bold, mono in parts:
        r = p.add_run()
        r.text = text
        f = r.font
        f.size = Pt(size)
        f.bold = bold
        f.name = MONO if mono else font
        f.color.rgb = color or default_color


def _markup(text):
    """`code` -> mono+blue, *bold* -> bold navy."""
    parts, buf, i = [], "", 0
    while i < len(text):
        ch = text[i]
        if ch in "`*":
            end = text.find(ch, i + 1)
            if end > i:
                if buf:
                    parts.append((buf, None, False, False))
                    buf = ""
                inner = text[i + 1 : end]
                if ch == "`":
                    parts.append((inner, BLUE, False, True))
                else:
                    parts.append((inner, NAVY, True, False))
                i = end + 1
                continue
        buf += ch
        i += 1
    if buf:
        parts.append((buf, None, False, False))
    return parts


def slide(title=None, kicker=None, footer=True):
    s = prs.slides.add_slide(BLANK)
    _box(s, 0, 0, W, H, fill=WHITE)
    if title is not None:
        _box(s, M, Inches(0.62), Inches(0.09), Inches(0.72), fill=YELLOW)
        tf = _tf(s, M + Inches(0.26), Inches(0.5), BODY_W - Inches(0.26), Inches(1.0))
        if kicker:
            _para(tf, kicker.upper(), 12, BLUE, bold=True, first=True, space_after=2)
            _para(tf, title, 30, NAVY, bold=True)
        else:
            _para(tf, title, 30, NAVY, bold=True, first=True)
    if footer and _section["name"]:
        tf = _tf(s, M, H - Inches(0.52), BODY_W, Inches(0.3))
        _para(tf, _section["name"], 10, GRAY, first=True)
    return s


def bullets(s, items, x=None, y=None, w=None, size=18, gap=9):
    """items: str, or (str, sub_level)."""
    x = M if x is None else x
    y = BODY_TOP if y is None else y
    w = BODY_W if w is None else w
    tf = _tf(s, x, y, w, H - y - Inches(0.7))
    first = True
    for it in items:
        text, lvl = (it, 0) if isinstance(it, str) else it
        if text == "":
            _para(tf, "", 6, GRAY, first=first)
            first = False
            continue
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.space_before = Pt(0 if p is tf.paragraphs[0] else gap)
        p.space_after = Pt(0)
        p.level = lvl
        p.alignment = PP_ALIGN.LEFT
        glyph = "▸  " if lvl == 0 else "        –  "
        r = p.add_run()
        r.text = glyph
        r.font.size = Pt(size - (2 if lvl else 0))
        r.font.name = SANS
        r.font.color.rgb = BLUE if lvl == 0 else GRAY
        r.font.bold = lvl == 0
        _rich(p, _markup(text), size - (2 if lvl else 0), NAVY if lvl == 0 else GRAY)
    return tf


def code(s, lines, x=None, y=None, w=None, size=15, caption=None, dark=True):
    x = M if x is None else x
    y = BODY_TOP if y is None else y
    w = BODY_W if w is None else w
    lh = Pt(size * 1.42).emu
    h = Emu(int(lh * len(lines)) + Inches(0.46).emu)
    _box(
        s,
        x,
        y,
        w,
        h,
        fill=NAVY if dark else LIGHT,
        shape=MSO_SHAPE.ROUNDED_RECTANGLE,
        radius=0.045,
    )
    tf = _tf(s, x + Inches(0.22), y + Inches(0.2), w - Inches(0.4), h - Inches(0.3))
    for i, ln in enumerate(lines):
        col = CODE_FG if dark else NAVY
        if ln.strip().startswith("#"):
            col = RGBColor(0x8E, 0xA6, 0xBD) if dark else GRAY
        _para(
            tf, ln if ln else " ", size, col, font=MONO, first=(i == 0), space_after=0
        )
    if caption:
        ctf = _tf(s, x, y + h + Inches(0.06), w, Inches(0.3))
        _para(ctf, caption, 13, GRAY, first=True, italic=True)
    return y + h + (Inches(0.42) if caption else Inches(0.24))


def out(s, lines, x=None, y=None, w=None, size=15, label="Output"):
    x = M if x is None else x
    w = BODY_W if w is None else w
    lh = Pt(size * 1.42).emu
    h = Emu(int(lh * len(lines)) + Inches(0.62).emu)
    _box(
        s,
        x,
        y,
        w,
        h,
        fill=LIGHT,
        line=RGBColor(0xD5, 0xDE, 0xE6),
        shape=MSO_SHAPE.ROUNDED_RECTANGLE,
        radius=0.045,
    )
    tf = _tf(s, x + Inches(0.22), y + Inches(0.16), w - Inches(0.4), h - Inches(0.26))
    _para(tf, label.upper(), 10, GRAY, bold=True, first=True, space_after=3)
    for ln in lines:
        _para(tf, ln if ln else " ", size, NAVY, font=MONO)
    return y + h + Inches(0.24)


def table(
    s,
    headers,
    rows,
    x=None,
    y=None,
    w=None,
    size=14,
    col_w=None,
    mono_cols=(),
    height=None,
):
    x = M if x is None else x
    y = BODY_TOP if y is None else y
    w = BODY_W if w is None else w
    h = height or Inches(0.42 + 0.36 * len(rows))
    shp = s.shapes.add_table(len(rows) + 1, len(headers), x, y, w, h)
    tbl = shp.table
    tbl.first_row = True
    if col_w:
        total = sum(col_w)
        for i, cw in enumerate(col_w):
            tbl.columns[i].width = Emu(int(w * cw / total))
    for j, htxt in enumerate(headers):
        c = tbl.cell(0, j)
        c.text = ""
        c.fill.solid()
        c.fill.fore_color.rgb = NAVY
        c.margin_left = c.margin_right = Inches(0.1)
        c.vertical_anchor = MSO_ANCHOR.MIDDLE
        _para(c.text_frame, htxt, size, WHITE, bold=True, first=True)
    for i, row in enumerate(rows, start=1):
        for j, val in enumerate(row):
            c = tbl.cell(i, j)
            c.text = ""
            c.fill.solid()
            c.fill.fore_color.rgb = WHITE if i % 2 else LIGHT
            c.margin_left = c.margin_right = Inches(0.1)
            c.margin_top = c.margin_bottom = Inches(0.03)
            c.vertical_anchor = MSO_ANCHOR.MIDDLE
            p = c.text_frame.paragraphs[0]
            mono = j in mono_cols
            _rich(
                p, _markup(val) if not mono else [(val, BLUE, False, True)], size, NAVY
            )
    return y + h + Inches(0.2)


def note(s, text, y, kind="tip"):
    colors = {
        "tip": (BLUE, "TIP"),
        "warn": (RED, "WATCH OUT"),
        "ok": (GREEN, "REMEMBER"),
    }
    col, label = colors[kind]
    h = Inches(0.78)
    _box(s, M, y, BODY_W, h, fill=LIGHT, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.06)
    _box(s, M, y, Inches(0.07), h, fill=col)
    tf = _tf(
        s,
        M + Inches(0.26),
        y + Inches(0.1),
        BODY_W - Inches(0.5),
        h - Inches(0.2),
        anchor=MSO_ANCHOR.MIDDLE,
    )
    _para(tf, label, 10, col, bold=True, first=True, space_after=2)
    p = tf.add_paragraph()
    _rich(p, _markup(text), 15, NAVY)
    return y + h + Inches(0.2)


def section(name, subtitle, points):
    _section["n"] += 1
    _section["name"] = name
    s = prs.slides.add_slide(BLANK)
    _box(s, 0, 0, W, H, fill=NAVY)
    _box(s, 0, H - Inches(0.22), W, Inches(0.22), fill=YELLOW)
    tf = _tf(s, M, Inches(2.1), Inches(8.4), Inches(3.0))
    _para(tf, f"PART {_section['n']}", 16, YELLOW, bold=True, first=True, space_after=8)
    _para(tf, name, 44, WHITE, bold=True, space_after=10)
    _para(tf, subtitle, 19, RGBColor(0xA9, 0xBD, 0xD1))
    tf2 = _tf(s, Inches(9.0), Inches(2.3), Inches(3.6), Inches(3.0))
    _para(tf2, "IN THIS PART", 11, YELLOW, bold=True, first=True, space_after=10)
    for pt in points:
        _para(tf2, "•  " + pt, 15, RGBColor(0xD6, 0xE2, 0xEC), space_after=7)
    return s


def flow(s, start, question, yes, no, y=None):
    """A read -> decide -> two outcomes diagram, the shape of every `if`."""
    y = BODY_TOP if y is None else y
    cy = y + Inches(0.7)

    def _label(shape_box, text, size=14, color=NAVY, bold=False):
        tf = _tf(
            s,
            shape_box[0],
            shape_box[1],
            shape_box[2],
            shape_box[3],
            anchor=MSO_ANCHOR.MIDDLE,
        )
        _para(tf, text, size, color, bold=bold, first=True, align=PP_ALIGN.CENTER)

    b = (M, cy - Inches(0.4), Inches(2.5), Inches(0.8))
    _box(
        s,
        *b,
        fill=LIGHT,
        line=RGBColor(0xC8, 0xD4, 0xDE),
        shape=MSO_SHAPE.ROUNDED_RECTANGLE,
        radius=0.12,
    )
    _label(b, start)

    _box(
        s,
        M + Inches(2.6),
        cy - Inches(0.13),
        Inches(0.5),
        Inches(0.26),
        fill=BLUE,
        shape=MSO_SHAPE.RIGHT_ARROW,
    )

    d = (M + Inches(3.25), cy - Inches(0.72), Inches(3.1), Inches(1.44))
    _box(s, *d, fill=YELLOW, shape=MSO_SHAPE.DIAMOND)
    _label(d, question, size=14, bold=True)

    _box(
        s,
        M + Inches(6.5),
        cy - Inches(0.13),
        Inches(0.6),
        Inches(0.26),
        fill=GREEN,
        shape=MSO_SHAPE.RIGHT_ARROW,
    )
    tfy = _tf(s, M + Inches(6.4), cy - Inches(0.52), Inches(0.8), Inches(0.3))
    _para(tfy, "yes", 12, GREEN, bold=True, first=True, align=PP_ALIGN.CENTER)

    yb = (M + Inches(7.25), cy - Inches(0.4), Inches(4.0), Inches(0.8))
    _box(
        s,
        *yb,
        fill=LIGHT,
        line=RGBColor(0xC8, 0xD4, 0xDE),
        shape=MSO_SHAPE.ROUNDED_RECTANGLE,
        radius=0.12,
    )
    _label(yb, yes, color=GREEN, bold=True)

    _box(
        s,
        M + Inches(4.67),
        cy + Inches(0.78),
        Inches(0.26),
        Inches(0.55),
        fill=RED,
        shape=MSO_SHAPE.DOWN_ARROW,
    )
    tfn = _tf(s, M + Inches(5.0), cy + Inches(0.9), Inches(0.8), Inches(0.3))
    _para(tfn, "no", 12, RED, bold=True, first=True)

    nb = (M + Inches(2.8), cy + Inches(1.42), Inches(4.0), Inches(0.8))
    _box(
        s,
        *nb,
        fill=LIGHT,
        line=RGBColor(0xC8, 0xD4, 0xDE),
        shape=MSO_SHAPE.ROUNDED_RECTANGLE,
        radius=0.12,
    )
    _label(nb, no, color=RED, bold=True)

    return cy + Inches(2.42)


# ============================================================== loop shape ==
def cycle(s, setup, test, body, step, done, y=None):
    """The shape every loop has: set up, test, run the body, come back."""
    y = BODY_TOP if y is None else y
    colw, gap = Inches(3.5), Inches(0.42)
    left = M + Inches(0.9)

    def _card(x, yy, w, h, text, fill, line, color, bold=True, size=14):
        _box(
            s,
            x,
            yy,
            w,
            h,
            fill=fill,
            line=line,
            shape=MSO_SHAPE.ROUNDED_RECTANGLE,
            radius=0.1,
        )
        tf = _tf(
            s,
            x + Inches(0.12),
            yy + Inches(0.08),
            w - Inches(0.24),
            h - Inches(0.16),
            anchor=MSO_ANCHOR.MIDDLE,
        )
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        _rich(p, _markup(text), size, color)

    h1 = Inches(0.62)
    _card(left, y, colw, h1, setup, LIGHT, RGBColor(0xC8, 0xD4, 0xDE), NAVY)

    ty = y + h1 + gap
    _box(s, left + Inches(1.55), y + h1, Inches(0.03), gap, fill=BLUE)
    _card(left, ty, colw, Inches(0.72), test, WHITE, BLUE, BLUE, size=15)

    by = ty + Inches(0.72) + gap
    _box(s, left + Inches(1.55), ty + Inches(0.72), Inches(0.03), gap, fill=BLUE)
    tfy = _tf(s, left + Inches(1.7), ty + Inches(0.74), Inches(1.4), Inches(0.3))
    _para(tfy, "still true", 11, GREEN, bold=True, first=True)
    _card(left, by, colw, Inches(0.62), body, LIGHT, RGBColor(0xC8, 0xD4, 0xDE), NAVY)

    sy = by + Inches(0.62) + gap
    _box(s, left + Inches(1.55), by + Inches(0.62), Inches(0.03), gap, fill=BLUE)
    _card(left, sy, colw, Inches(0.62), step, LIGHT, RGBColor(0xC8, 0xD4, 0xDE), NAVY)

    # the arrow that makes it a loop: back up from the step to the test
    back_x = left + colw + Inches(0.3)
    _box(s, back_x, ty + Inches(0.36), Inches(0.03), sy - ty - Inches(0.05), fill=BLUE)
    _box(s, left + colw, ty + Inches(0.36), Inches(0.33), Inches(0.03), fill=BLUE)
    _box(s, left + colw, sy + Inches(0.29), Inches(0.33), Inches(0.03), fill=BLUE)
    tfb = _tf(s, back_x + Inches(0.12), ty + Inches(1.1), Inches(1.9), Inches(0.4))
    _para(tfb, "and round again", 12, BLUE, bold=True, first=True)

    # the exit
    ex = left - Inches(0.1)
    tfe = _tf(s, left - Inches(0.85), ty + Inches(0.18), Inches(0.8), Inches(0.3))
    _para(tfe, "false", 11, RED, bold=True, first=True)
    _box(s, ex - Inches(0.62), ty + Inches(0.36), Inches(0.62), Inches(0.03), fill=RED)
    _card(
        left - Inches(0.62) - Inches(2.5),
        ty + Inches(0.08),
        Inches(2.5),
        Inches(0.6),
        done,
        LIGHT,
        RGBColor(0xE0, 0xB8, 0xB8),
        RED,
    )

    return sy + Inches(0.62) + Inches(0.3)


# ================================================================== TITLE ==
def title_slide():
    s = prs.slides.add_slide(BLANK)
    _box(s, 0, 0, W, H, fill=NAVY)
    _box(s, 0, H - Inches(0.28), W, Inches(0.28), fill=YELLOW)
    _box(s, M, Inches(1.5), Inches(0.12), Inches(1.5), fill=YELLOW)
    tf = _tf(s, M + Inches(0.4), Inches(1.4), Inches(9.5), Inches(2.0))
    _para(tf, "PYTHON · TOPIC 3", 15, YELLOW, bold=True, first=True, space_after=12)
    _para(tf, "Doing It Again", 52, WHITE, bold=True, space_after=10)
    _para(
        tf,
        "Loops: for, while, and the patterns built on them",
        22,
        RGBColor(0xA9, 0xBD, 0xD1),
    )
    tf2 = _tf(s, M + Inches(0.4), Inches(4.3), Inches(10.5), Inches(2.0))
    _para(
        tf2,
        "A computer is not faster than you at thinking.",
        18,
        RGBColor(0x8F, 0xB6, 0xD9),
        first=True,
        space_after=8,
    )
    _para(
        tf2,
        "It is faster than you at doing the same thing 10 000 times.",
        18,
        RGBColor(0x8F, 0xB6, 0xD9),
    )
    tf3 = _tf(s, M + Inches(0.4), Inches(6.2), Inches(10.0), Inches(0.5))
    _para(
        tf3,
        "python-workbook2026  ·  repetitions",
        13,
        RGBColor(0x6E, 0x8A, 0xA3),
        first=True,
    )


def roadmap_slide():
    s = slide("What we cover today", kicker="Roadmap", footer=False)
    table(
        s,
        ["Part", "Topic", "You will be able to"],
        [
            ["1", "*Why loops*", "say what a loop repeats and when it stops"],
            ["2", "*The `for` loop*", "count with `range` and walk a string"],
            ["3", "*The `while` loop*", "repeat until a condition changes"],
            ["4", "*`break` and `continue`*", "leave early, or skip one turn"],
            ["5", "*Accumulators*", "total, count, and find the largest"],
            ["6", "*Nested loops*", "print tables and shapes"],
        ],
        y=BODY_TOP,
        col_w=(0.8, 3.4, 7.0),
        size=16,
    )
    note(
        s,
        "Everything today sits on the `if` you already know — a loop is a "
        "decision asked over and over.",
        Inches(5.5),
        kind="ok",
    )


# =================================================================== PART 1 ==
def part1():
    section(
        "Why loops",
        "The same work, without writing it out",
        ["Copy-paste does not scale", "The anatomy of a loop", "`for` or `while`?"],
    )

    s = slide("Print the numbers 1 to 5", kicker="Without a loop")
    y = code(
        s,
        [
            "print(1)",
            "print(2)",
            "print(3)",
            "print(4)",
            "print(5)",
        ],
        w=Inches(5.6),
    )
    code(
        s,
        [
            "for i in range(1, 6):",
            "    print(i)",
        ],
        x=M + Inches(6.1),
        y=BODY_TOP,
        w=Inches(5.6),
    )
    y = out(s, ["1", "2", "3", "4", "5"], y=y + Inches(0.1), w=Inches(5.6))
    note(
        s,
        "Now make it 1 to 1000. The left column needs 995 more lines; the "
        "right one needs *one character*.",
        Inches(5.4),
        kind="tip",
    )

    s = slide("Every loop has four parts", kicker="Anatomy")
    cycle(
        s,
        setup="start: `total = 0`, `i = 1`",
        test="is the condition still true?",
        body="do the work — the *body*",
        step="change something: `i = i + 1`",
        done="leave the loop",
        y=Inches(1.6),
    )
    note(
        s,
        "Forget the *step* and the condition never changes — that is an "
        "infinite loop, and the program hangs.",
        Inches(6.1),
        kind="warn",
    )

    s = slide("Two loops, two questions", kicker="Choosing")
    table(
        s,
        ["Question", "Loop", "Example"],
        [
            ["I know *how many times*", "`for`", "print a table of 12 rows"],
            [
                "I repeat *until something changes*",
                "`while`",
                "read numbers until the user types 0",
            ],
        ],
        col_w=(4.2, 1.6, 5.4),
        size=17,
    )
    y = bullets(
        s,
        [
            "A `for` loop counts through a sequence that already exists",
            "A `while` loop keeps going while a condition holds",
            "Anything a `for` can do, a `while` can do — it is just longer to write",
        ],
        y=Inches(3.9),
        size=18,
    )
    note(
        s,
        "Rule of thumb: if you can say the number of turns out loud before "
        "the loop starts, use `for`.",
        Inches(5.8),
        kind="ok",
    )


# =================================================================== PART 2 ==
def part2():
    section(
        "The `for` loop",
        "Counting through a sequence",
        ["`range` with 1, 2, 3 arguments", "Walking a string", "The loop variable"],
    )

    s = slide("for ... in range(...)", kicker="Syntax")
    y = code(
        s,
        [
            "for i in range(1, 6):",
            "    print(i)",
            "",
            "# i takes each value in turn: 1, 2, 3, 4, 5",
            "# the indented block runs once per value",
        ],
    )
    y = out(s, ["1", "2", "3", "4", "5"], y=y)
    note(
        s,
        "The colon and the indentation are the same rules as `if`. The "
        "indented block is the *body*.",
        y,
        kind="ok",
    )

    s = slide("range() takes up to three numbers", kicker="range")
    table(
        s,
        ["Call", "Produces", "Read it as"],
        [
            ["`range(5)`", "0 1 2 3 4", "five values, starting at 0"],
            ["`range(1, 6)`", "1 2 3 4 5", "from 1, *stop before* 6"],
            ["`range(0, 101, 10)`", "0 10 20 ... 100", "from 0 to 100, step 10"],
            ["`range(5, 0, -1)`", "5 4 3 2 1", "count down, step -1"],
            ["`range(0)`", "nothing", "an empty range — the body never runs"],
        ],
        col_w=(2.6, 3.4, 5.2),
        size=16,
        mono_cols=(),
    )
    note(
        s,
        "The stop value is never reached. `range(1, 6)` ends at 5 — this is "
        "the single most common off-by-one in the chapter.",
        Inches(4.9),
        kind="warn",
    )

    s = slide("A string is a sequence too", kicker="Iterating")
    y = code(
        s,
        [
            'word = "loop"',
            "",
            "for letter in word:",
            "    print(letter)",
        ],
        w=Inches(6.0),
    )
    out(s, ["l", "o", "o", "p"], x=M + Inches(6.4), y=BODY_TOP, w=Inches(5.2))
    y = bullets(
        s,
        [
            "No `range`, no counting — `for` walks the characters directly",
            "The loop variable is *yours* to name: `letter` says more than `i`",
            "`len(word)` still tells you how many turns there will be",
        ],
        y=y + Inches(0.3),
        size=18,
    )
    note(
        s,
        "`for i in range(len(word)):` also works, but then you need "
        "`word[i]`. Walk the string directly when you can.",
        Inches(5.7),
        kind="tip",
    )


# =================================================================== PART 3 ==
def part3():
    section(
        "The `while` loop",
        "Repeating until something changes",
        ["Syntax and the counter", "Reading until a sentinel", "Infinite loops"],
    )

    s = slide("while <condition>:", kicker="Syntax")
    y = code(
        s,
        [
            "i = 1                 # set up",
            "",
            "while i <= 5:         # test, every turn",
            "    print(i)          # body",
            "    i = i + 1         # step — without this it never ends",
        ],
    )
    y = out(s, ["1", "2", "3", "4", "5"], y=y)
    note(
        s,
        "Same output as the `for` above, three extra lines. That is why "
        "counting jobs belong to `for`.",
        y,
        kind="tip",
    )

    s = slide("Reading until the user stops", kicker="Sentinel")
    y = code(
        s,
        [
            "number = int(input())",
            "",
            "while number != 0:",
            "    print(number * 2)",
            "    number = int(input())",
            "",
            "print('done')",
        ],
        w=Inches(6.4),
    )
    out(
        s,
        ["4      <- typed", "8", "7      <- typed", "14", "0      <- typed", "done"],
        x=M + Inches(6.8),
        y=BODY_TOP,
        w=Inches(4.8),
        label="A session",
    )
    note(
        s,
        "This is the shape of every sentinel loop: *read once before* the "
        "loop, and *read again at the end of the body*.",
        y + Inches(0.1),
        kind="ok",
    )

    s = slide("The loop that never ends", kicker="Watch out")
    y = code(
        s,
        [
            "i = 1",
            "while i <= 5:",
            "    print(i)",
            "    # i never changes -> the condition is always true",
        ],
        w=Inches(6.4),
    )
    out(
        s,
        ["1", "1", "1", "1", "1", "..."],
        x=M + Inches(6.8),
        y=BODY_TOP,
        w=Inches(4.8),
        label="Forever",
    )
    y = bullets(
        s,
        [
            "Press *Ctrl + C* in the terminal to stop a runaway program",
            "Before you run a `while`, find the line that moves it towards the end",
            "If the condition can never become false, the loop is a bug",
        ],
        y=y + Inches(0.25),
        size=18,
    )


# =================================================================== PART 4 ==
def part4():
    section(
        "break and continue",
        "Leaving early, skipping a turn",
        ["`break` stops the loop", "`continue` skips one turn", "When not to use them"],
    )

    s = slide("break — stop the whole loop", kicker="break")
    y = code(
        s,
        [
            "for n in range(100, 200):",
            "    if n % 7 == 0:",
            "        print(n)",
            "        break            # found it, nothing left to do",
        ],
        w=Inches(6.4),
    )
    out(s, ["105"], x=M + Inches(6.8), y=BODY_TOP, w=Inches(4.8))
    note(
        s,
        "Without `break` the loop would keep running through 199 and print "
        "every multiple of 7.",
        y + Inches(0.1),
        kind="tip",
    )

    s = slide("continue — skip this one, keep going", kicker="continue")
    y = code(
        s,
        [
            "for n in range(1, 11):",
            "    if n % 2 == 0:",
            "        continue         # even -> jump to the next n",
            "    print(n)",
        ],
        w=Inches(6.4),
    )
    out(s, ["1", "3", "5", "7", "9"], x=M + Inches(6.8), y=BODY_TOP, w=Inches(4.8))
    y = bullets(
        s,
        [
            "`break` leaves the loop; `continue` only ends the *current turn*",
            "Both work in `for` and in `while`",
            "In a `while`, a `continue` that skips the step gives an infinite loop",
        ],
        y=y + Inches(0.15),
        size=18,
    )
    note(
        s,
        "The same output comes from `if n % 2 == 1: print(n)` — often the "
        "plain condition reads better than `continue`.",
        Inches(5.9),
        kind="ok",
    )


# =================================================================== PART 5 ==
def part5():
    section(
        "Accumulator patterns",
        "Four loops you will write all year",
        ["Total", "Count", "Largest and smallest", "Building a string"],
    )

    s = slide("Pattern 1 — a running total", kicker="Accumulate")
    y = code(
        s,
        [
            "total = 0                    # start empty",
            "",
            "for i in range(1, 6):",
            "    total = total + i        # add this turn's value",
            "",
            "print(total)",
        ],
        w=Inches(6.4),
    )
    out(s, ["15"], x=M + Inches(6.8), y=BODY_TOP, w=Inches(4.8))
    note(
        s,
        "The variable is created *before* the loop and printed *after* it. "
        "Put either one inside, and the answer is wrong.",
        y + Inches(0.1),
        kind="warn",
    )

    s = slide("Pattern 2 — counting matches", kicker="Count")
    y = code(
        s,
        [
            'word = "repetition"',
            "vowels = 0",
            "",
            "for letter in word:",
            '    if letter in "aeiou":',
            "        vowels = vowels + 1",
            "",
            "print(vowels)",
        ],
        w=Inches(6.4),
    )
    out(s, ["5"], x=M + Inches(6.8), y=BODY_TOP, w=Inches(4.8))
    note(
        s,
        "A loop with an `if` inside it — the two topics meet here, and most "
        "exercises from now on look like this.",
        y + Inches(0.1),
        kind="ok",
    )

    s = slide("Pattern 3 — the largest so far", kicker="Min / max")
    y = code(
        s,
        [
            "largest = int(input())       # the first value is the champion",
            "",
            "for _ in range(4):",
            "    value = int(input())",
            "    if value > largest:",
            "        largest = value      # a new champion",
            "",
            "print(largest)",
        ],
        w=Inches(6.8),
    )
    out(
        s,
        ["5  12  3  8  15", "", "15"],
        x=M + Inches(7.2),
        y=BODY_TOP,
        w=Inches(4.4),
        label="In / out",
    )
    note(
        s,
        "Never start `largest` at 0 — all-negative input would then give a "
        "wrong answer. Start from the *first value read*.",
        y + Inches(0.1),
        kind="warn",
    )

    s = slide("The four patterns side by side", kicker="Summary")
    table(
        s,
        ["Goal", "Before the loop", "Inside the loop"],
        [
            ["total", "`total = 0`", "`total = total + value`"],
            ["count", "`count = 0`", "`if ...: count = count + 1`"],
            ["largest", "`largest = first value`", "`if value > largest: ...`"],
            ["text", '`line = ""`', "`line = line + piece`"],
        ],
        col_w=(2.2, 4.0, 5.0),
        size=16,
    )
    note(
        s,
        "Every one of them: create it before, change it inside, use it "
        "after. Learn the shape, not the four separate recipes.",
        Inches(4.6),
        kind="ok",
    )


# =================================================================== PART 6 ==
def part6():
    section(
        "Nested loops",
        "A loop inside a loop",
        ["Rows and columns", "Printing on one line", "Reading the output"],
    )

    s = slide("A loop inside a loop", kicker="Nesting")
    y = code(
        s,
        [
            "for row in range(1, 4):",
            "    for col in range(1, 4):",
            "        print(row * col, end=' ')",
            "    print()              # end the row",
        ],
        w=Inches(6.4),
    )
    out(s, ["1 2 3", "2 4 6", "3 6 9"], x=M + Inches(6.8), y=BODY_TOP, w=Inches(4.8))
    y = bullets(
        s,
        [
            "The *inner* loop runs all the way through for every single outer turn",
            "3 rows × 3 columns = 9 prints",
            "`print()` with nothing in it ends the line and starts the next row",
        ],
        y=y + Inches(0.1),
        size=18,
    )

    s = slide("print(end=...) keeps the line open", kicker="Output")
    y = code(
        s,
        [
            "for i in range(1, 6):",
            "    print(i, end=' ')",
            "print()",
        ],
        w=Inches(6.0),
    )
    out(s, ["1 2 3 4 5"], x=M + Inches(6.4), y=BODY_TOP, w=Inches(5.2))
    y = code(
        s,
        [
            "for i in range(1, 6):",
            "    print(i)",
        ],
        y=y + Inches(0.2),
        w=Inches(6.0),
    )
    out(
        s,
        ["1", "2", "3", "4", "5"],
        x=M + Inches(6.4),
        y=y - Inches(1.3),
        w=Inches(5.2),
    )
    note(
        s,
        "By default `print` ends with a newline. `end=' '` replaces it with "
        "a space — the rest of the line stays open.",
        Inches(6.0),
        kind="tip",
    )

    s = slide("Build a triangle", kicker="Patterns")
    y = code(
        s,
        [
            "for row in range(1, 5):",
            "    for star in range(row):",
            "        print('*', end='')",
            "    print()",
        ],
        w=Inches(6.4),
    )
    out(s, ["*", "**", "***", "****"], x=M + Inches(6.8), y=BODY_TOP, w=Inches(4.8))
    note(
        s,
        "The inner loop's count depends on the outer variable — `range(row)` "
        "is what makes the shape grow.",
        y + Inches(0.1),
        kind="ok",
    )


# ================================================================= CLOSING ==
def closing():
    s = prs.slides.add_slide(BLANK)
    _box(s, 0, 0, W, H, fill=NAVY)
    _box(s, 0, H - Inches(0.28), W, Inches(0.28), fill=YELLOW)
    tf = _tf(s, Inches(1.3), Inches(1.5), Inches(10.7), Inches(3.6))
    _para(tf, "Your turn", 44, WHITE, bold=True, first=True, space_after=18)
    _para(
        tf,
        "Start with right_triangle and temperature_table, then work down "
        "the table of contents.",
        22,
        RGBColor(0xC3, 0xD3, 0xE1),
        space_after=26,
    )
    _para(
        tf,
        "Before you write a loop, answer three questions: what repeats, "
        "what changes each turn, and what makes it stop.",
        17,
        RGBColor(0x8F, 0xB6, 0xD9),
    )
    tf2 = _tf(s, Inches(1.3), Inches(5.5), Inches(10.7), Inches(1.2))
    _para(
        tf2,
        "uv run pytest repetitions/",
        18,
        YELLOW,
        bold=True,
        first=True,
        space_after=10,
    )
    _para(tf2, "Good luck  ·  see you soon", 20, YELLOW, bold=True)


# ==================================================================== main ==
title_slide()
roadmap_slide()
part1()
part2()
part3()
part4()
part5()
part6()
closing()

prs.save(OUT)
print(f"{len(prs.slides)} slides -> {OUT}")
