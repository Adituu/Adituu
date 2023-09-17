import string

from Cryptodome.Random import random


def generate_secure_string(charset: str = string.ascii_letters + string.digits, length: int = 32) -> str:
    return ''.join(random.sample(charset, k=length))


def generate_secure_filename(filename: str, length: int = 8) -> str:
    return generate_secure_string(length=length) + f".{filename.rsplit('.', 1)[1]}"


if __name__ == '__main__':
    print(generate_secure_string())
    print(generate_secure_filename('asdf.png'))
