"""
Provides encryption and decryption with the atbash cipher
"""
import string

# create alphabet dict
ALPHABET = {}
for i, letter in enumerate(string.ascii_lowercase):
    ALPHABET[letter] = string.ascii_lowercase[-i-1]
for i, letter in enumerate(string.ascii_uppercase):
    ALPHABET[letter] = string.ascii_uppercase[-i-1]


def encrypt(inp: str) -> str:
    """
    Encrypts a given input with the atbash cipher

    Parameters
    ----------
    inp: str
        The text you want to encrypt
    """
    if not inp.isalpha():
        return None
    return "".join([ALPHABET[x] for x in inp])


def decrypt(inp: str) -> str:
    """
    Decrypts a given input with the atbash cipher

    Parameters
    ----------
    inp: str
        The text you want to decrypt
    """
    return encrypt(inp)
