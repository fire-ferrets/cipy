"""
Vigenere cipher

Allows you to encrypt and decrypt text with the Vigenere cipher
"""


def encrypt(msg: str, key: str) -> str:
    """
    Encrypt a message using a Vigenere encryption

    Parameters
    ----------
    msg: str
        The message you want to encrypt
    key: str
        The key you want to use to encrypt
    """
    if not msg.replace(" ", "a").isalpha() or not key.isalpha():
        return None
    msg = msg.upper()
    key = key.upper()
    key_length = len(key)
    secret = ""
    skip = 0
    for i, letter in enumerate(msg):
        if letter == " ":
            secret += " "
            skip += 1
        else:
            secret += chr(((ord(letter) + ord(key[(i - skip) % key_length]) - 130) % 26) + 65)
    return secret


def decrypt(msg: str, key: str) -> str:
    """
    Decrypt a message that is Vigenere encrypted

    Parameters
    ----------
    msg: str
        The message you want to decrypt
    key: str
        The key you want to use to decrypt
    """
    if not msg.replace(" ", "a").isalpha() or not key.isalpha():
        return None
    msg = msg.upper()
    key = key.upper()
    key_length = len(key)
    plain = ""
    skip = 0
    for i, letter in enumerate(msg):
        if letter == " ":
            plain += " "
            skip += 1
        else:
            plain += chr(((ord(letter) - ord(key[(i - skip) % key_length]) - 130) % 26) + 65)
    return plain
