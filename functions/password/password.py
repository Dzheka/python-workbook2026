import string
import random

def password(length: int) -> str:
    pool = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(pool) for _ in range(length))
