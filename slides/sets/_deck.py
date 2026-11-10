"""Drawing primitives shared by the decks in this folder.

Each topic folder keeps its own copy of this file so a deck builds from its
folder alone; keep the copies in step when the look changes.

One module-level ``prs`` is created on import, which is what the build scripts
want: one process builds one deck and calls ``save()`` at the end.
"""

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Emu, Inches, Pt

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


def save(path):
    prs.save(path)
    return len(prs.slides._sldIdLst)


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
