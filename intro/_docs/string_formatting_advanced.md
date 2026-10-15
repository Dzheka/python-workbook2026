# F-String Formatting Advanced

Complete reference for advanced Python f-string formatting features.

## Format Specifier Syntax

| Component   | Syntax                                                                    | Purpose                       |
|-------------|---------------------------------------------------------------------------|-------------------------------|
| Full format | `f"{value:[[fill]align][sign][#][0][width][grouping][.precision][type]}"` | Complete format specification |

## Width and Alignment

| Format    | Description            | Example            | Output       |
|-----------|------------------------|--------------------|--------------|
| `{n:5}`   | Minimum width 5        | `f"{42:5}"`        | `   42`      |
| `{n:05}`  | Width 5, zero-padded   | `f"{42:05}"`       | `00042`      |
| `{s:<10}` | Left align, width 10   | `f"{'hello':<10}"` | `hello     ` |
| `{s:>10}` | Right align, width 10  | `f"{'hello':>10}"` | `     hello` |
| `{s:^10}` | Center align, width 10 | `f"{'hello':^10}"` | `  hello   ` |
| `{n:=5}`  | Sign-aware padding     | `f"{-42:=5}"`      | `-  42`      |

## Custom Fill Characters

| Format    | Description              | Example        | Output  |
|-----------|--------------------------|----------------|---------|
| `{n:*<5}` | Left align with * fill   | `f"{42:*<5}"`  | `42***` |
| `{n:*>5}` | Right align with * fill  | `f"{42:*>5}"`  | `***42` |
| `{n:*^5}` | Center align with * fill | `f"{42:*^5}"`  | `*42**` |
| `{n:*=5}` | Sign-aware with * fill   | `f"{-42:*=5}"` | `-**42` |

## Number Base Formatting

| Format   | Description             | Example      | Output     |
|----------|-------------------------|--------------|------------|
| `{n:b}`  | Binary                  | `f"{42:b}"`  | `101010`   |
| `{n:o}`  | Octal                   | `f"{42:o}"`  | `52`       |
| `{n:x}`  | Hexadecimal (lowercase) | `f"{42:x}"`  | `2a`       |
| `{n:X}`  | Hexadecimal (uppercase) | `f"{42:X}"`  | `2A`       |
| `{n:#b}` | Binary with prefix      | `f"{42:#b}"` | `0b101010` |
| `{n:#o}` | Octal with prefix       | `f"{42:#o}"` | `0o52`     |
| `{n:#x}` | Hex with prefix         | `f"{42:#x}"` | `0x2a`     |

## Scientific and Engineering Notation

| Format    | Description               | Example           | Output         |
|-----------|---------------------------|-------------------|----------------|
| `{n:e}`   | Scientific (lowercase)    | `f"{1234.5:e}"`   | `1.234500e+03` |
| `{n:E}`   | Scientific (uppercase)    | `f"{1234.5:E}"`   | `1.234500E+03` |
| `{n:.2e}` | Scientific with precision | `f"{1234.5:.2e}"` | `1.23e+03`     |
| `{n:g}`   | General format            | `f"{1234.5:g}"`   | `1234.5`       |
| `{n:.3g}` | General with 3 sig figs   | `f"{1234.5:.3g}"` | `1.23e+03`     |

## Sign Handling

| Format  | Description                  | Example     | Output |
|---------|------------------------------|-------------|--------|
| `{n:+}` | Always show sign             | `f"{42:+}"` | `+42`  |
| `{n:-}` | Show negative only (default) | `f"{42:-}"` | `42`   |
| `{n: }` | Space for positive           | `f"{42: }"` | ` 42`  |

## Grouping and Separators

| Format     | Description                    | Example                | Output         |
|------------|--------------------------------|------------------------|----------------|
| `{n:,}`    | Thousands separator            | `f"{1234567:,}"`       | `1,234,567`    |
| `{n:_}`    | Underscore separator           | `f"{1234567:_}"`       | `1_234_567`    |
| `{n:,.2f}` | Float with thousands separator | `f"{1234567.89:,.2f}"` | `1,234,567.89` |

## Percentage Formatting

| Format     | Description               | Example            | Output       |
|------------|---------------------------|--------------------|--------------|
| `{n:%}`    | Percentage                | `f"{0.1234:%}"`    | `12.340000%` |
| `{n:.2%}`  | Percentage with precision | `f"{0.1234:.2%}"`  | `12.34%`     |
| `{n:+.1%}` | Percentage with sign      | `f"{0.1234:+.1%}"` | `+12.3%`     |

## String Manipulation

| Format             | Description         | Example                     | Output  |
|--------------------|---------------------|-----------------------------|---------|
| `{s:.5}`           | Truncate to 5 chars | `f"{'Hello World':.5}"`     | `Hello` |
| `{s.upper()}`      | Uppercase           | `f"{'alice'.upper()}"`      | `ALICE` |
| `{s.lower()}`      | Lowercase           | `f"{'ALICE'.lower()}"`      | `alice` |
| `{s.title()}`      | Title case          | `f"{'alice'.title()}"`      | `Alice` |
| `{s.capitalize()}` | Capitalize first    | `f"{'alice'.capitalize()}"` | `Alice` |

## Nested F-Strings

| Pattern           | Description             | Example                    | Output                 |
|-------------------|-------------------------|----------------------------|------------------------|
| Dynamic precision | Variable decimal places | `f"{value:.{precision}f}"` | `Depends on precision` |
| Dynamic width     | Variable field width    | `f"{'Hello':{width}}"`     | `Depends on width`     |
| Dynamic format    | Variable format type    | `f"{num:{fmt}}"`           | `Depends on fmt`       |

## Date and Time Formatting

| Format           | Description  | Example              | Output           |
|------------------|--------------|----------------------|------------------|
| `{dt:%Y-%m-%d}`  | ISO date     | `f"{now:%Y-%m-%d}"`  | `2024-03-15`     |
| `{dt:%H:%M:%S}`  | Time         | `f"{now:%H:%M:%S}"`  | `14:30:25`       |
| `{dt:%B %d, %Y}` | Full date    | `f"{now:%B %d, %Y}"` | `March 15, 2024` |
| `{dt:%A}`        | Weekday name | `f"{now:%A}"`        | `Friday`         |

## Special Characters and Escaping

| Pattern          | Description    | Example                    | Output              |
|------------------|----------------|----------------------------|---------------------|
| `{{}}`           | Literal braces | `f"{{Hello}}"`             | `{Hello}`           |
| `{var} {{text}}` | Mixed braces   | `f"Value: {42} {{units}}"` | `Value: 42 {units}` |
| Raw f-strings    | Backslashes    | `rf"{path}\file.txt"`      | `C:\Users\file.txt` |

## Complex Table Formatting

| Use Case   | Format Pattern                            | Example                     |
|------------|-------------------------------------------|-----------------------------|
| Header row | `f"{'Item':<10} {'Qty':>5} {'Price':>8}"` | `Item         Qty    Price` |
| Data rows  | `f"{item:<10} {qty:>5} ${price:>7.2f}"`   | `Apples         5 $   1.25` |
| Separator  | `"-" * total_width`                       | `-------------------------` |

## Multi-line Formatting Examples

| Pattern          | Code                                                      | Output                                       |
|------------------|-----------------------------------------------------------|----------------------------------------------|
| Student record   | `f"Student: {name:<10} Score: {score:6.1f} ({pct:6.1%})"` | `Student: Alice      Score:   87.5 ( 87.5%)` |
| Scientific data  | `f"Standard: {val:,.2f}\nScientific: {val:.2e}"`          | `Standard: 1,234.57<br>Scientific: 1.23e+03` |
| Financial report | `f"${amount:>10,.2f}"`                                    | `$  1,234.56`                                |

This reference covers advanced f-string formatting for complex layouts, scientific notation, custom alignment, and
specialized formatting needs.
