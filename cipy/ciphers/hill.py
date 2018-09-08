"""
Hill Cipher

Allows you to encrypt and decrypt messages with the Hill cipher
"""
import numpy as np
from .. import alphabet as alphb

def _mod_inverse(a: int, n: int) -> int:
    t, newt = 0, 1
    r, newr = n, a
    while newr != 0:
        quotient = r // newr
        t, newt = newt, t - quotient * newt
        r, newr = newr, r - quotient * newr
    if r > 1:
        return "a is not invertible"
    elif t < 0:
        t = t + n
    return t


def _mod_inv_matrix(matrix: np.ndarray, m: int) -> np.ndarray:
    det = np.linalg.det(matrix)
    cofactor = np.linalg.inv(matrix).T * det
    inv = _mod_inverse(int(det), m)
    inv_matrix = inv * cofactor
    inv_matrix = np.around(np.mod(inv_matrix, m)).astype(int).T
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
    crypt_mat = np.mod(np.dot(key, msg_vector).astype(int), len(A))
    crypt_msg = [A[c] for c in crypt_mat]
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
    key = _mod_inv_matrix(key, len(alphabet))
    return encrypt(msg, key, alphabet)

