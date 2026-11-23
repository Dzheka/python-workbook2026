import random
import string
def password(n):
    pas=""
    pun="!@#$%^&*()"
    ch = string.ascii_lowercase+ string.ascii_uppercase + string.digits + pun
    for i in range(n):
        pas += random.choice(ch)
    return pas