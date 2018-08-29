"""
Provides encryption and decryption with the atbash cipher
"""
import string

# create alphabet dict
ALPHABET = {c: string.ascii_lowercase[-i-1] for i, c in enumerate(string.ascii_lowercase)}
ALPHABET.update({c: string.ascii_uppercase[-i-1] for i, c in enumerate(string.ascii_uppercase)})


def encrypt(msg: str) -> str:
    """
    Encrypt a message using an Atbash encryption

    Parameters
    ----------
    msg: str
        The message you want to encrypt
    """
    if not msg.isalpha():
        return None
    return "".join([ALPHABET[x] for x in msg])


def decrypt(msg: str) -> str:
    """
    Decrypt a message that is Atbash encrypted

    Parameters
    ----------
    msg: str
        The message you want to decrypt
    """
    return encrypt(msg)
