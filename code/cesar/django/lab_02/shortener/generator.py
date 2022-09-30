import random
import string


def token_generator():
    characters = string.ascii_lowercase + string.ascii_uppercase
    return print(''.join(random.choice(characters) for i in range(6)))


token_generator()
