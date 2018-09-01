"""
One time pad cipher

Allows you to encrypt and decrypt text with the one time pad cipher
"""


def encrypt(msg: str, key: str) -> str:
    """
    Encrypt a message using a one time pad encryption

    Parameters
    ----------
    msg: str
        The message you want to encrypt
    key: str
        The key you want to use to encrypt
    """
    if not all(x.isspace() or x.isalpha for x in key) or not all(x.isspace() or x.isalpha() for x in msg):
        return None
    msg = msg.upper()
    key = key.upper()
    secret = ""
    skip = 0
    for i, letter in enumerate(msg):
        if letter == " ":
            secret += " "
            skip += 1
        else:
            secret += chr(((ord(letter) + ord(key[i - skip]) - 130) % 26) + 65)
    return secret


def decrypt(msg: str, key: str) -> str:
    """
    Decrypt a message that is one time pad encrypted

    Parameters
    ----------
    msg: str
        The message you want to decrypt
    key: str
        The key you want to use to decrypt
    """
    if not all(x.isspace() or x.isalpha for x in key) or not all(x.isspace() or x.isalpha() for x in msg):
        return None
    msg = msg.upper()
    key = key.upper()
    plain = ""
    skip = 0
    for i, letter in enumerate(msg):
        if letter == " ":
            plain += " "
            skip += 1
        else:
            plain += chr(((ord(letter) - ord(key[i - skip]) - 130) % 26) + 65)
    return plain
