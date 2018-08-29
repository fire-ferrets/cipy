"""
Rail fence cipher

Allows you to encrypt and decrypt text with the rail fence cipher
"""


def _get_indices(msg: str, key: int) -> list:
    """
    Gets encrypted indice to a given message and key.

    Returns a list of rows with the indice of the msgut letters
    if they were encrypted.
    The list will be in the format
    [[index1, index2, ...], [index3, index4, ...], ...]
    with 'key' elements

    Parameters
    ----------
    msg: str
        The message string
    key: int
        The key to en- / decrypt
    """
    length = len(msg)
    dif_first_row = 2 * key - 2
    indice = [[] for i in range(key)]
    # calculate indice for text splitting
    indice[0] = [x for x in range(0, length, dif_first_row)]
    for x in range(1, key):
        for y in indice[0]:
            if y + x < length and y + x not in indice[x]:
                indice[x].append(y + x)
            if y + dif_first_row - x < length and y + dif_first_row - x not in indice[x]:
                indice[x].append(y + dif_first_row -x)
    return indice


def encrypt(msg: str, key: int) -> str:
    """
    Encrypt a message using a Rail Fence encryption

    Parameters
    ----------
    msg: str
        The message you want to encrypt
    key: int
        The key to encrypt
    """
    msg = msg.strip()
    indice = _get_indices(msg, key)
    ret = ""
    for row in indice:
        for index in row:
            ret += msg[index]
    return ret


def decrypt(msg: str, key: int) -> str:
    """
    Decrypt a message that is Rail Fence encrypted

    Parameters
    ----------
    msg: str
        The message you want to decrypt
    key: int
        The key to decrypt
    """
    msg = msg.strip()
    indice = _get_indices(msg, key)
    all_indice = []
    for x in indice:
        all_indice += x
    ret = ""
    for i in range(len(msg)):
        ret += msg[all_indice.index(i)]
    return ret
