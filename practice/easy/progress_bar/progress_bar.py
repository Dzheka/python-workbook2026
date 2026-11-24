def progress_bar(percent, width):
    percent = max(0, min(100, percent))

    num_hashes = (percent * width) // 100
    num_dashes = width - num_hashes

    bar = "#" * num_hashes + "-" * num_dashes
    return f"[{bar}] {percent}%"