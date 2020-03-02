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
            print("Invalid Key")
            return -1
        pattern.append(alpha.find(letter))
    return pattern

class transposition:

    def encode(key, message):
        
    