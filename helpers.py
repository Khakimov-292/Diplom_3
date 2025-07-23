import string
import random

EMAIL_LEN = 6


def generate_email():
    chars = string.ascii_lowercase + string.digits
    email = ''.join(random.choice(chars) for _ in range(EMAIL_LEN))
    return f"{email}@ya.ru"


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string
