"""
ASCII cipher

Allows you to encrypt and decrypt text using the ASCII cipher
"""


def encrypt(msg: str) -> str:
    """
    Encrypt a message using an ASCII encryption

    Parameters
    ----------
    msg: str
        The message you want to encrypt
    """
    return " ".join([str(ord(x)) for x in msg])


def decrypt(msg: str) -> str:
    """
    Decrypt a message that is ASCII encrypted

    Parameters
    ----------
    msg: str
        The message you want to decrypt
    """
    return "".join([chr(int(x)) for x in msg.split(" ")])
