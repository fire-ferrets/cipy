"""
Vigenere cipher

Allows you to encrypt and decrypt text with the Vigenere cipher
"""


def encrypt(inp: str, key: str) -> str:
    """
    Encrypts a given input text with a given key

    Parameters
    ----------
    inp: str
        The text you want to encrypt
    key: str
        The key you want to use to encrypt
    """
    if not inp.replace(" ", "a").isalpha() or not key.isalpha():
        return None
    inp = inp.upper()
    key = key.upper()
    key_length = len(key)
    secret = ""
    skip = 0
    for i, letter in enumerate(inp):
        if letter == " ":
            secret += " "
            skip += 1
        else:
            secret += chr(((ord(letter) + ord(key[(i - skip) % key_length]) - 130) % 26) + 65)
    return secret


def decrypt(inp: str, key: str) -> str:
    """
    Decrypts a given text with a given key

    Parameters
    ----------
    inp: str
        The text you want to decrypt
    key: str
        The key you want to use to decrypt
    """
    if not inp.replace(" ", "a").isalpha() or not key.isalpha():
        return None
    inp = inp.upper()
    key = key.upper()
    key_length = len(key)
    plain = ""
    skip = 0
    for i, letter in enumerate(inp):
        if letter == " ":
            plain += " "
            skip += 1
        else:
            plain += chr(((ord(letter) - ord(key[(i - skip) % key_length]) - 130) % 26) + 65)
    return plain
