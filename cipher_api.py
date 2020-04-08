from ciphers.caesar import caesar
from ciphers.vignere import vignere
from ciphers.transposition import transposition
from ciphers.combo import combo
from ciphers.feistel import feistel

methods = ['Caesar', 'Vignere', 'Transposition', 'Combo', 'Feistel']

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


method_classes = [caesar, vignere, transposition, combo, feistel]
overview = [
    'A simple substitution cipher. Key is of type int.', 
    'A Substitution cipher. Key is a string containing only letters.', 
    'A transposition cipher. Key is a string conatining only letters.', 
    'A cipher that combines both the vignere and the transposition cipher.', 
    'A feistel network. Randomized layered encryption using multiple methods and different keys. Input key is a sentence.'
    ]
in_depth = [
    'Caesar', 
    'Vignere', 
    'Transposition', 
    'Combo', 
    'Feistel'
    ]