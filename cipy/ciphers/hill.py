"""
Hill Cipher

Allows you to encrypt and decrypt messages with the Hill cipher
"""
import numpy as np
from .. import alphabet


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
    A = alphabet.Alphabet(alphabet)
    msg_vector = np.array([A[c] for c in msg])[:, np.newaxis]
    crypt_mat = np.dot(key, msg_vector)
    def mat_mod(x):
        return A[x % len(key)]

    mat_mod = np.vectorize(mat_mod)
    crypt_msg = mat_mod(crypt_mat)
    return "".join([c for c in crypt_msg])


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
    key = np.linalg.inv(key)
    return encrypt(msg, key, alphabet)

