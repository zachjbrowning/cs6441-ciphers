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
    'The caesar cipher is a very basic substitution. It works by shifting the alphabet along a given number of letters, and substituing these new letters to convert from a plaintext to a ciphertext. The number of times the alphabet is shifted across is the key.', 
    'The vignere cipher is a substitution cipher that provides a more complex iteration on the caesar cipher. Rather than the alphabet being shifted the same for each letter, a key provides a set of different shifts that are applied in order for each different letter of the plaintext. In this instance, the key is a word, with each letter in the word representing a different shift. In this way the plaintext is substitued into a ciphertext, with different parts of the plaintext being substitued with different alphabets.', 
    'The transposition cipher offers a different kind of encryption to substitution ciphers. The transposition cipher works by rearranging the position of the letters in the plaintext to produce a ciphertext. This is done by forming a matrix out of the plaintext letters with dimensions as square as possible. The key, in this implementation being a word, provides a new ordering of the rows and columns to produce the ciphertext.', 
    'The combo method brings together both the caesar and transposition cipher. The aim of this cipher is to fill in the flaws of one method using the other and vice versa. The implementation works simply by using the same key, encrypting the plaintext once and then encrypting the produced ciphertext again using the other method.', 
    'A feistel network is a method used to layer encryption by doing multiple rounds of encryption using different keys. The plaintext is halved and encrypted seperately. Importantly, the keys for each round of encryption comes from an operation completed on the other half of the text, meaning the keys for each round of encryption cannot be sourced without being able to encrypt and generate those keys. This implementation uses the previously mentioned ciphers as methods. The plaintext is split up into two equal parts. The key is a sentence. The first word of the sentence decides the order in which the different methods are used for each round of encryption. Each other word represents a round, with one half of the text being encrypted using that rounds word and previusly chosen method, to produce a new key. This new key is then used to encrypt the other half of the text with the same method. This is done for each extra word in the sentence key. As a result, the longer the sentence, the higher level of security in the encryption.',
    ]