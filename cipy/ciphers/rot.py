r"""
ROT Cipher

This file provides functionality for dealing with ROT ciphers
"""

def encipher(msg: str, key: int, alphabet="abcdefghijklmnopqrstuvwxyz": str):
    """
    Encipher a message using a ROT encryption

    This function enciphers a provided message with a given key
    by using a ROT encryption.

    Parameters
    ----------
    msg : string
        The message that is to be enciphered
    key : int
        The amount of shifting to be done
    alphabet : string
        The alphabet that shall be used in the encryption.
        It should not contain repeating characters.

    Returns
    -------
    string
        The enciphered message
    """
    cipher_msg = ""
    for c in msg:
        pos = alphabet.index(c)
        pos = (pos + key) % len(alphabet)
        cipher = alphabet[pos]
        cipher_msg = "".join((cipher_msg, cipher))
    return cipher_msg

def decipher(msg: str, key: int, alphabet="abcdefghijklmnopqrstuvwxyz": str):
    """
    Decipher a message with a ROT encryption

    This function enciphers a provided message with a given key
    by using a ROT encryption.

    Parameters
    ----------
    msg : string
        The message that is to be deciphered
    key : int
        The amount of shifting that has been done
    alphabet : string
        The alphabet that shall be used in the encryption.
        It should not contain repeating characters.

    Returns
    -------
    string
        The deciphered message
    """
    decipher_msg = ""
    for c in msg:
        pos = alphabet.index(c)
        pos = (pos + key) % len(alphabet)
        decipher = alphabet[pos]
        decipher_msg = "".join((decipher_msg, decipher))
    return decipher_msg
