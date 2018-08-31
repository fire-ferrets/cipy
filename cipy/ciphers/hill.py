"""
Hill Cipher

Allows you to encrypt and decrypt messages with the Hill cipher
"""
import numpy as np
from .. import alphabet as alphb

def _mod_inverse(a, n):
    t, newt = 0, 1
    r, newr = n, a
    while newr != 0:
        quotient = r % newr
        t, newt = newt, t - quotient * newt
        r, newr = newr, r - quotient * newr
    if r > 1:
        return "a is not invertible"
    elif t < 0:
        t = t + n
    return t


def _mod_inv_matrix(matrix, m):
    det = int(np.linalg.det(matrix))
    print(det)
    cofactor = (np.linalg.inv(matrix).T * det).astype(int)
    inv = _mod_inverse(det, m)
    print(cofactor)
    print(inv)
    inv_matrix = inv * cofactor
    inv_matrix = np.mod(inv_matrix, m)
    return inv_matrix



def encrypt(msg: str, key: np.ndarray, alphabet: str) -> str:
    """
    Encrypt a message using a Hill encryption

    Parameters
    ----------
    msg : str
        The message you want to encrypt
    key : np.ndarray
        An invertible NxN np.array. N denotes the length of :code:`msg`
    alphabet : str
        The alphabet you want to use
    """
    A = alphb.Alphabet(alphabet)
    msg_vector = np.array([A[c] for c in msg])
    crypt_mat = np.dot(msg_vector, key).astype(int)
    crypt_msg = [A[c % len(alphabet)] for c in crypt_mat]
    print("crypt_msg", crypt_msg)
    return "".join(crypt_msg)


def decrypt(msg: str, key: np.ndarray, alphabet: str) -> str:
    """
    Decrypt a message that is Hill encrypted

    Parameters
    ----------
    msg : str
        The message you want to encrypt
    key : np.ndarray
        An invertible NxN np.array. N denotes the length of :code:`msg`.
        The key that has been used for encryption.
    alphabet : str
        The alphabet you want to ues
    """
    key = _mod_inv_matrix(key, len(key))
    return encrypt(msg, key, alphabet)

