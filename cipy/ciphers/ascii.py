"""
ASCII cipher

Allows you to encrypt and decrypt text using the ASCII cipher
"""


def encrypt(inp: str) -> str:
    """
    Encrypts a given input with the ascii cipher

    Parameters
    ----------
    inp: str
        The text you want to encrypt
    """
    return " ".join([str(ord(x)) for x in inp])


def decrypt(inp: str) -> str:
    """
    Decrypts a given input with the ascii cipher

    Parameters
    ----------
    inp: str
        The text you want to decrypt
    """
    return "".join([chr(int(x)) for x in inp.split(" ")])
