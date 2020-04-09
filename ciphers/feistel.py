from .vignere import vignere
from .transposition import transposition
from .combo import combo 
import math as m

def ordering(keylist):
    order = keylist[0]
    for letter in order:
        if not letter.isalpha():
            raise KeyError("Key must be alphabetic only!")
    orderkey = list((order * m.ceil((len(keylist) - 1) / len(order)))[:len(keylist) - 1])
    uniquekey = []  
    for i in range(len(orderkey)):
        uniquekey.insert(0, orderkey.pop() + str(i))

    uniquekeyORD = sorted([x for x in uniquekey])

    result = []
    for item in uniquekeyORD:
        result.append(uniquekey.index(item) % 3)
    return result

def prep(keylist, message):
    if len(message) % 2 == 1:
        message += ' '
    cipher_order = ordering(keylist)
    cipher_keys = keylist[1:]
    return message, cipher_order, cipher_keys

def feistel_forward(former, latter, cipher_order, cipher_keys, ciphers):
    for i in range(len(cipher_keys)):
        if i % 2 == 0:
            newkey = ciphers[cipher_order[i]].encode(cipher_keys[i], latter)
            newkey = "".join(newkey.split())
            former = ciphers[cipher_order[i]].encode(newkey, former)
        else:
            newkey = ciphers[cipher_order[i]].encode(cipher_keys[i], former)
            newkey = "".join(newkey.split())
            latter = ciphers[cipher_order[i]].encode(newkey, latter)
    return former, latter


def feistel_back(former, latter, cipher_order, cipher_keys, ciphers):
    i = len(cipher_keys) - 1
    while i >= 0:

        if i % 2 == 0:
            newkey = ciphers[cipher_order[i]].encode(cipher_keys[i], latter)
            
            newkey = "".join(newkey.split())
            former = ciphers[cipher_order[i]].decode(newkey, former)
        else:
            newkey = ciphers[cipher_order[i]].encode(cipher_keys[i], former)
            newkey = "".join(newkey.split())
            latter = ciphers[cipher_order[i]].decode(newkey, latter)
        i -= 1 
    return former, latter

class feistel:
    def encode(key, message):
        message, cipher_order, cipher_keys = prep(key.split(), message)
        former = message[:len(message) // 2]
        latter = message[len(message) // 2:]
        ciphers = [vignere, transposition, combo]
        former, latter = feistel_forward(former, latter, cipher_order, cipher_keys, ciphers)
        msg = str(former) + '?' + str(latter)
        return msg
    def decode(key, message):
        discard, cipher_order, cipher_keys = prep(key.split(), message)
        parts = message.split('?')
        if len(parts) != 2:
            raise ValueError("Message is not decodable. It is corrupted")
        former = parts[0]
        latter = parts[1]
        ciphers = [vignere, transposition, combo]
        former, latter = feistel_back(former, latter, cipher_order, cipher_keys, ciphers)
        return former + latter
        