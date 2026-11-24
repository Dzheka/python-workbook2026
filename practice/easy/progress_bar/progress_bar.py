def progress_bar(percent, width):
    percent = max(0, min(percent, 100))
    a = percent * width // 100
    b = "#" * a + "-" * (width - a)
    return f"[{b}] {percent}%"