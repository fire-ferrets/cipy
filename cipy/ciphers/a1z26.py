"""
A1Z26 Cipher

Allows you to encrypt and decrypt text with the A1Z26 cipher
"""
import string
from .. import alphabet
ALPHABET = " " + string.ascii_uppercase


def encrypt(msg: str) -> str:
    """
    Encrypt a message using a A1Z26 encryption

    Parameters
    ----------
    msg: str
        The message you want to encrypt
    """
    if not all(x.isalpha() or x.isspace() for x in msg):
        return None
    msg = msg.upper()
    numbers = [str(ALPHABET.index(x)) for x in msg]
    return " ".join(numbers)


def decrypt(msg: str) -> str:
    """
    Decrypt a message that is A1Z26 encrypted

    Parameters
    ----------
    msg: str
        The message you want to decrypt
    """
    if not all(x.isdigit() or x.isspace() for x in msg):
        return None
    letters = [ALPHABET[int(x)] for x in msg.split(" ")]
    return "".join(letters)
