import random
import string


def generate_name():
    return ''.join(random.sample(string.ascii_letters + string.digits, 15))
