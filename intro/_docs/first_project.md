# Creating Your First Python Project

This guide will walk you through creating and running your first Python program.

## Create Your First Python Project

1. Open Terminal
2. Navigate to where you want to create your project (ex. `~/repos`):
   ```
   cd ~/repos
   ```
3. Create a new Python project with uv:
   ```
   uv init first-project
   ```
4. Move into your new project folder:
   ```
   cd first-project
   ```

## Open Your Project in VS Code

1. While in your project folder in the terminal, type:
   ```
   code .
   ```
   (This opens the current folder in VS Code)

2. If VS Code doesn't open, you can:
    - Open VS Code manually
    - Go to File → Open Folder
    - Select your `first-project` folder

## Understanding Your Project

When you used `uv init`, it created several files:

- `pyproject.toml` - Contains project settings
- `.python-version` - Contains the python version
- `README.md` - Information about your project
- `main.py` - A sample Python file

## Write Your First Program

1. Open the `main.py` file (it should already exist)
2. Replace its contents with:

```python
print("Hello, World!")
print("I'm learning Python!")
```

## Run Your Program

1. In VS Code, open the terminal (Terminal → New Terminal)
2. Run your program with:
   ```
   uv run main.py
   ```
3. You should see your messages printed in the terminal

## What Just Happened?

- **uv init** created a complete Python project structure for you
- **VS Code** is where you write and edit your code
- **uv run** executes your Python programs in the project's managed environment
- **Python** is the language that understands your code and makes it work

## Working With the Workbook Exercises

Each exercise lives in its own folder and contains:

- `exercise_name.md` - The problem description
- `exercise_name.py` - The file where you write your solution
- `test_exercise_name.py` - Automated tests that check your solution

### How to Read an Exercise

Each `exercise_name.md` ends with an **Examples** section. An example has up
to two code blocks:

```
5.2
```

```
The area is: 84.95
```

- The **first block** is the input you type while the program runs — one
  value per line, pressing **Enter** after each. (If an exercise needs no
  input, like `hello_world`, this block is omitted.)
- The **second block** is exactly what your program must print.

You do **not** have to write a prompt string, and if you do, the wording is
yours to choose. All of these are accepted:

```python
radius = float(input("Enter radius: "))  # prompt is fine
radius = float(input("Radius? "))        # any wording is fine
radius = float(input())                  # no prompt is also fine
```

The checker never sees your prompts. It compares only the
values you read and the output you print. Some exercises still show prompts
in their examples (e.g. multi-value ones like `bmi`); those prompts are
optional too.

### Run an Exercise

Open the exercise folder, write your code in the `.py` file, then run it:

```
uv run intro/hello_world/hello_world.py
```

### Test Your Solution

Tests are written with `pytest`. To check a single exercise:

```
uv run pytest intro/hello_world/
```

To run every test in a chapter:

```
uv run pytest intro/
```

A passing test means your solution produces the expected output. A failing
test shows what was expected versus what your program actually printed.

## Common Commands You'll Use

- `cd` - **C**hange **D**irectory
- `uv init project-name` - Create a new Python project
- `code .` - Open the current folder in VS Code
- `uv run main.py` - Run a Python file
- `uv run pytest path/to/exercise/` - Test an exercise solution

Congratulations! You now have a proper Python development setup, and you're ready to start programming.
