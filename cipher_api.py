from ciphers.transposition import hello_world



"""
Available methods for encoding and decoding:
    vignere:
        - key must be a string of purely alphabetic letters (typically a word)
    caeser:
        - key must be an integer

"""


def encode(method, key, msg):
    return method.encode(key, msg)

def decode(method, key, msg):
    return method.decode(key, msg)