"""
RSA cipher

Allows you to encrypt and decrypt text with the RSA cipher
At the moment only allows to encrypt ASCII text
"""
import math


def _gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common denominator for two given numbers

    Parameters
    ----------
    a : int
        the first number you want to test
    b : int
        the second number you want to test
    """
    while b != 0:
        a, b = b, a % b
    return a


def _check_if_prime(num: int) -> bool:
    """
    Check whether a natural number is a prime

    Parameters
    ----------
    num : int
        the number you want to test
    """
    if num < 2 or num % 2 == 0:
        return False
    if num == 2:
        return True
    for x in range(3, int(math.sqrt(num)), 2):
        if num % x == 0:
            return False
    return True


def encrypt(msg: str, n: int, e: int) -> str:
    """
    Encrypt a message with your private RSA key

    Parameters
    ----------
    msg : str
        the message you want to encrypt
    n : int
        the modulus n of your keypair
    e : int
        the public exponent e of your public key
    """
    secret_msg = " ".join([(ord(x) ** e) % n for x in msg])
    return secret_msg


def decrypt(msg: str, n: int, d: int) -> str:
    """
    Decrypt a message with your private RSA key

    Parameters
    ----------
    msg : str
        the message you want to encrypt
    n : int
        the modulus n of your keypair
    d : int
        the secret exponent d of your private key
    """
    plain_msg = "".join(chr((x ** d) % n) for x in msg.split(" "))
    return plain_msg


def gen_keypair() -> dict:
    """
    Generates a keypair

    Returns
    -------
    t: (n, e, d)
    """
    pass
