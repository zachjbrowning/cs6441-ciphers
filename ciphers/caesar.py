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


class caesar:

    def encode(key, message):
        try:
            key = int(key)
        except ValueError:
            raise KeyError("Key must be of type int")
        answer = ''
        for letter in message:
            answer += moveChar(letter, key)
        return answer 

    def decode(key, message):
        answer = ''
        for letter in message:
            answer += moveChar(letter, -key)
        return answer