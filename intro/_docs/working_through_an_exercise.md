# Working Through an Exercise

Each exercise lives in its own folder. Inside, you'll find a problem
statement (`<name>.md`) and a test file (`test_<name>.py`). You write the
solution file yourself, naming it after the folder.

## Read the Problem

Start by reading the problem statement. It explains what your program
should do and shows you examples of the expected input and output.

For example, open `conditionals/leap_year/leap_year.md` before writing any
code.

## Write Your Solution

Create the solution file in the same folder, named after the folder.

For the `leap_year` exercise, that means creating
`conditionals/leap_year/leap_year.py`.

## Run Your Program

Run your program manually to see it in action:

```
uv run conditionals/leap_year/leap_year.py
```

`uv run` installs any dependencies automatically, so there's no separate
install step.

## Check Your Work with the Tests

Once you're happy with your solution, run the tests to check it:

```
uv run pytest conditionals/leap_year
```

## Reading the Examples

Problem statements show examples as pairs of plain code blocks. The first
block is what you type as input while your program runs. The second block
is the exact output your program must print.

Here's the example from `leap_year`:

```
2000
```

```
Leap year
```

## Reading Test Results

- **passed** - your output matches the expected output exactly
- **failed** - your output doesn't match; read the diff to see what was
  expected versus what your program actually printed
- **skipped** with "Solution file not found" - you haven't created the
  solution file yet. Skipped does **not** mean passed!

Tests compare your output *exactly*. Spacing, capitalization, and
punctuation all matter.

## Stuck?

If you get stuck, reference solutions live on the `solutions` branch:

```
git switch solutions
```

When you're ready to come back to your own work:

```
git switch main
```

Try to solve each exercise honestly before peeking. You'll learn a lot more
that way.

You've got this! Every exercise you finish makes the next one a little easier.
