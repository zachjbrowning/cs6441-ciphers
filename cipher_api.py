from ciphers.caesar import caesar
from ciphers.vignere import vignere
from ciphers.transposition import transposition
from ciphers.combo import combo
from ciphers.feistel import feistel



"""
Available methods for encoding and decoding:
    vignere:
        - key must be a string of purely alphabetic letters and spaces
    caeser:
        - key must be an integer
    key_transpose:
        - key must be a string of purely alphabetic letters and spaces
    combo:
        -key must be a string of purely alphabetic letters and spaces
    feistel:
        -key must be a string of preferrably multiple words, each only containing alphabetic letters
"""
methods = ['Caesar', 'Vignere', 'Transposition', 'Combo', 'Feistel']
method_classes = [caesar, vignere, transposition, combo, feistel]
documentation = ['Simple subsitution cipher. Key is of type Int.', 'Substitution cipher. Key is a string containing only letters.', 'Transposition cipher. Key is a string conatining only letters.', 'Combination using both the vignere and the transposition cipher.', 'Feistel network. Randomized layered encryption using multiple methods and different keys']

def encode(method, key, msg):
    try:
        result = method.encode(key, msg)
    except KeyError as oops:
        return oops
    return result

def decode(method, key, msg):
    try:
        result = method.decode(key, msg)
    except KeyError as oops:
        return oops
    return result