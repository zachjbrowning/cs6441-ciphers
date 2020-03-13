import string

def moveChar(letter, shift):
    if letter.isalpha() is False:
        return letter
    alpha = string.ascii_uppercase
    if letter.isupper() is False:
        alpha = string.ascii_lowercase
    
    index = alpha.find(letter)
    index += shift
    index = index % len(alpha)
    return alpha[index]

def getPattern(key):
    key = key.upper()
    alpha = string.ascii_uppercase
    pattern = []
    for letter in key:
        
        if letter.isalpha() is False:
            raise KeyError("Key must be alphabetic only!")
        pattern.append(alpha.find(letter))
    return pattern

class vignere:

    def encode(key, message):
        newmessage = ''
        pattern = getPattern(key)
        i = 0
        for letter in message:
            if letter.isalpha():
                newmessage += moveChar(letter, pattern[i])
                i = (i + 1) % len(pattern)
            else:
                newmessage += letter
        return newmessage

    def decode(key, message):
        newmessage = ''
        pattern = getPattern(key)
        pattern = [-x for x in pattern]
        i = 0
        for letter in message:
            if letter.isalpha():
                newmessage += moveChar(letter, pattern[i])
                i = (i + 1) % len(pattern)
            else:
                newmessage += letter
        return newmessage


