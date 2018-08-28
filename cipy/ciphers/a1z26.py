"""
A1Z26 Cipher

Allows you to encrypt and decrypt text with the A1Z26 cipher
"""
import string
ALPHABET = " " + string.ascii_uppercase


def encrypt(inp: str) -> str:
    """
    Encrypts a given input text

    Parameters
    ----------
    inp: str
        The text you want to encrypt
    """
    if not inp.replace(" ", "").isalpha():
        return None
    inp = inp.upper()
    numbers = [str(ALPHABET.index(x)) for x in inp]
    return " ".join(numbers)


def decrypt(inp: str) -> str:
    """
    Decrypts a given input text

    Parameters
    ----------
    inp: str
        The text you want to decrypt
    """
    if not inp.replace(" ", "").isdigit():
        return None
    letters = [ALPHABET[int(x)] for x in inp.split(" ")]
    return "".join(letters)
