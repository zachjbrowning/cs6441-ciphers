from ciphers.transposition import hello_world



"""
Available methods for encoding and decoding:
    - transposition:
        - key must be of type int, specifying the amount the alphabet should be shifted across.


"""


def encode(method, key, msg):
    return method.encode(key, msg)

def decode(method, key, msg):
    return method.decode(key, msg)