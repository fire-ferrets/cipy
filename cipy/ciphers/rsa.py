"""
RSA cipher

Allows you to encrypt and decrypt text with the RSA cipher
"""

def encrypt(msg: str, n: int, e: int) -> str:
    """
    Encrypt a message with your private RSA key

    Parameters
    ----------
    msg: str
        the message you want to encrypt
    n: int
        the modulus n of your keypair
    e: int
        the public exponent e of your public key
    """
    pass


def decrypt(msg: str, n: int, d: int) -> str:
    """
    Decrypt a message with your private RSA key

    Parameters
    ----------
    msg: str
        the message you want to encrypt
    n: int
        the modulus n of your keypair
    d: int
        the secret exponent d of your private key
    """
    pass


def gen_keypair() -> dict:
    """
    Generates a keypair

    Returns
    -------
    t: (n, e, d)
    """
    pass
