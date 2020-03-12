from .vignere import vignere
from .transposition import transposition






class combo:
    def encode(key, message):
        return vignere.encode(key, transposition.encode(key, message))

    def decode(key, message):
        return transposition.decode(key, vignere.decode(key, message))