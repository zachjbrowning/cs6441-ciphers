from ciphers.caesar import caesar
from ciphers.vignere import vignere
from ciphers.transposition import transposition



"""
Available methods for encoding and decoding:
    vignere:
        - key must be a string of purely alphabetic letters 
    caeser:
        - key must be an integer
    key_transpose:
        - key must be a string of purely alphabetic letters
"""


def encode(method, key, msg):
    return method.encode(key, msg)

def decode(method, key, msg):
    return method.decode(key, msg)