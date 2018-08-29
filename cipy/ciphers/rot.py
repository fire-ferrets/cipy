r"""
ROT Cipher

This file provides functionality for dealing with ROT ciphers
"""

def encrypt(msg: str, key: int, alphabet: str="abcdefghijklmnopqrstuvwxyz") -> str:
    """
    Encrypt a message using a ROTX encryption

    This function enciphers a provided message with a given key
    by using a ROT encryption.

    Parameters
    ----------
    msg : string
        The message you want to encrypt
    key : int
        The amount of shifting to be done
    alphabet : string
        The alphabet that shall be used in the encryption.
        It should not contain repeating characters.

    Returns
    -------
    string
        The encrypted message
    """
    cipher_msg = ""
    for c in msg:
        pos = alphabet.index(c)
        pos = (pos + key) % len(alphabet)
        cipher = alphabet[pos]
        cipher_msg = "".join((cipher_msg, cipher))
    return cipher_msg

def decrypt(msg: str, key: int, alphabet: str="abcdefghijklmnopqrstuvwxyz") -> str:
    """
    Decrypt a message that is ROTX encrypted

    This function enciphers a provided message with a given key
    by using a ROT encryption.

    Parameters
    ----------
    msg : string
        The message you want to decrypt
    key : int
        The amount of shifting that has been done
    alphabet : string
        The alphabet that shall be used in the encryption.
        It should not contain repeating characters.

    Returns
    -------
    string
        The decrypted message
    """
    decipher_msg = ""
    for c in msg:
        pos = alphabet.index(c)
        pos = (pos + key) % len(alphabet)
        decipher = alphabet[pos]
        decipher_msg = "".join((decipher_msg, decipher))
    return decipher_msg
