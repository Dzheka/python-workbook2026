# Python Workbook 2026 — Intro

Сборник задач по Python с автоматической проверкой. Первая тема — **intro**:
переменные, типы, ввод/вывод, арифметика, форматирование строк.

## 1. Регистрация на GitHub

1. Открой https://github.com/signup
2. Введи почту, придумай пароль и username (латиницей, например `ivan-petrov`).
3. Подтверди почту по коду из письма.
4. Готово — аккаунт есть.

## 2. Установи программы

**Git** — https://git-scm.com/downloads (Windows: ставь со всеми галочками по умолчанию).

**uv** — менеджер Python-проектов, сам поставит нужный Python.

- macOS / Linux:
  ```
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
- Windows (PowerShell):
  ```
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```

**VS Code** — https://code.visualstudio.com + расширение **Python** от Microsoft.

Проверь, что всё встало (перезапусти терминал):

```
git --version
uv --version
```

## 3. Сделай свою копию репозитория (fork)

1. Открой https://github.com/Dzheka/python-workbook2026
2. Жми **Fork** (справа сверху) → **Create fork**.
3. Теперь репозиторий есть у тебя: `https://github.com/ТВОЙ-USERNAME/python-workbook2026`

## 4. Скачай его на компьютер (clone)

В терминале (подставь свой username):

```
git clone https://github.com/ТВОЙ-USERNAME/python-workbook2026.git
cd python-workbook2026
code .
```

## 5. Реши первую задачу

Каждая задача — отдельная папка. Внутри:

- `hello_world.md` — условие
- `test_hello_world.py` — тест, который проверит решение
- `hello_world.py` — **этот файл создаёшь ты сам**, имя = имя папки

Порядок работы:

1. Прочитай условие: `intro/hello_world/hello_world.md`
2. Создай файл `intro/hello_world/hello_world.py` и напиши решение:
   ```python
   print("Hello, World!")
   ```
3. Запусти:
   ```
   uv run intro/hello_world/hello_world.py
   ```
4. Проверь тестом:
   ```
   uv run pytest intro/hello_world/
   ```

## 6. Как читать условие

В конце каждой задачи есть блок **Examples** — до двух блоков кода:

- **первый** — что ты вводишь с клавиатуры (по одному значению на строку, Enter после каждого);
  если ввода нет (как в `hello_world`), блока нет;
- **второй** — что программа должна напечатать, **точь-в-точь**.

Текст подсказки в `input()` писать не обязательно, проверка его не видит:

```python
radius = float(input("Введи радиус: "))  # можно
radius = float(input())                   # тоже можно
```

Регистр, пробелы и знаки препинания в выводе важны.

## 7. Результаты тестов

- **passed** — вывод совпал, задача решена
- **failed** — не совпал, смотри в diff: что ожидалось и что напечатала твоя программа
- **skipped** («Solution file not found») — ты ещё не создал файл с решением.
  Skipped ≠ passed!

Запустить все задачи темы сразу:

```
uv run pytest intro/
```

## 8. Сохрани работу на GitHub

```
git add .
git commit -m "solve hello_world"
git push
```

Первый раз git спросит логин — вводи username и **personal access token**
вместо пароля (GitHub → Settings → Developer settings → Personal access tokens
→ Tokens (classic) → Generate new token, галочка `repo`).

## Шпаргалка по командам

| Команда | Что делает |
| --- | --- |
| `cd имя_папки` | зайти в папку |
| `code .` | открыть текущую папку в VS Code |
| `uv run путь/к/файлу.py` | запустить программу |
| `uv run pytest intro/задача/` | проверить одну задачу |
| `uv run pytest intro/` | проверить всю тему |
| `git add . && git commit -m "..." && git push` | сохранить работу на GitHub |

## Полезное

- `intro/_docs/first_project.md` — первый проект с нуля, подробно
- `intro/_docs/working_through_an_exercise.md` — как работать с задачей
- `intro/_docs/vars_and_types.md` — переменные и типы
- `intro/_docs/math_operators.md`, `math_functions.md` — арифметика
- `intro/_docs/string_formatting.md` — форматирование строк
