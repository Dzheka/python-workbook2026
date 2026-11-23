# Python Workbook 2026 — Intro

A collection of Python exercises with automated tests. First topic: **intro** —
variables, types, input/output, arithmetic, string formatting.

## 1. Create a GitHub account

1. Go to https://github.com/signup
2. Enter your email, pick a password and a username (latin letters, e.g. `ivan-petrov`).
3. Confirm your email with the code from the message.
4. Done — you have an account.

## 2. Install the tools

**Git** — https://git-scm.com/downloads (on Windows keep all default options).

**uv** — the Python project manager; it installs the right Python for you.

- macOS / Linux:
  ```
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
- Windows (PowerShell):
  ```
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```

**VS Code** — https://code.visualstudio.com plus the **Python** extension by Microsoft.

Restart your terminal, then check that everything is installed:

```
git --version
uv --version
```

## 3. Fork the repository

1. Open https://github.com/Dzheka/python-workbook2026
2. Click **Fork** (top right) → **Create fork**.
3. You now have your own copy at `https://github.com/YOUR-USERNAME/python-workbook2026`

## 4. Clone it to your computer

In the terminal (use your own username):

```
git clone https://github.com/YOUR-USERNAME/python-workbook2026.git
cd python-workbook2026
code .
```

## 5. Solve your first exercise

Every exercise lives in its own folder. Inside you'll find:

- `hello_world.md` — the problem statement
- `test_hello_world.py` — the test that checks your solution
- `hello_world.py` — **you create this file yourself**; its name matches the folder

How to work:

1. Read the statement: `intro/hello_world/hello_world.md`
2. Create `intro/hello_world/hello_world.py` and write your solution:
   ```python
   print("Hello, World!")
   ```
3. Run it:
   ```
   uv run intro/hello_world/hello_world.py
   ```
4. Check it with the test:
   ```
   uv run pytest intro/hello_world/
   ```

## 6. How to read a problem statement

Each exercise ends with an **Examples** section holding up to two code blocks:

- the **first** is what you type while the program runs — one value per line,
  pressing Enter after each; if the exercise needs no input (like `hello_world`),
  this block is omitted;
- the **second** is exactly what your program must print.

You don't have to write a prompt inside `input()` — the checker never sees it:

```python
radius = float(input("Enter radius: "))  # a prompt is fine
radius = float(input())                  # no prompt is fine too
```

Capitalization, spacing and punctuation in the output all matter.

## 7. Reading test results

- **passed** — your output matches; the exercise is solved
- **failed** — it doesn't match; read the diff to see expected vs. actual output
- **skipped** ("Solution file not found") — you haven't created the solution
  file yet. Skipped is **not** passed!

Run every exercise in the topic at once:

```
uv run pytest intro/
```

## 8. Push your work to GitHub

```
git add .
git commit -m "solve hello_world"
git push
```

The first time, git asks for credentials: use your username and a **personal
access token** instead of a password (GitHub → Settings → Developer settings →
Personal access tokens → Tokens (classic) → Generate new token, tick `repo`).

Every push runs the **Grade Calculator** automatically. Open the **Actions** tab
in your fork to see your grade — the report lists passed, failed and skipped
exercises and a percentage.

## 9. Submit your work with a Pull Request

When you want your work reviewed, open a pull request:

1. Go to your fork on GitHub: `https://github.com/YOUR-USERNAME/python-workbook2026`
2. Click **Contribute** → **Open pull request** (or the **Pull requests** tab → **New pull request**).
3. Check the direction: base repository `Dzheka/python-workbook2026` `main` ←
   head repository `YOUR-USERNAME/python-workbook2026` `main`.
4. Title it with your name and the topic, e.g. `Ivan Petrov — intro`.
5. Click **Create pull request**.

The grader runs on the pull request too, so the grade shows up right in it.
Keep pushing to your fork afterwards — new commits land in the same pull
request automatically, no need to open a second one.

## Command cheat sheet

| Command | What it does |
| --- | --- |
| `cd folder_name` | enter a folder |
| `code .` | open the current folder in VS Code |
| `uv run path/to/file.py` | run a program |
| `uv run pytest intro/exercise/` | test one exercise |
| `uv run pytest intro/` | test the whole topic |
| `git add . && git commit -m "..." && git push` | push your work to GitHub |

## Further reading

- `intro/_docs/first_project.md` — your first project from scratch, step by step
- `intro/_docs/working_through_an_exercise.md` — how to work through an exercise
- `intro/_docs/vars_and_types.md` — variables and types
- `intro/_docs/math_operators.md`, `math_functions.md` — arithmetic
- `intro/_docs/string_formatting.md` — string formatting
