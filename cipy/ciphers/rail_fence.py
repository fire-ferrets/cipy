"""
Rail fence cipher

Allows you to encrypt and decrypt text with the rail fence cipher
"""


def _get_indices(inp: str, key: int) -> list:
    """
    Gets encrypted indice to a given input and key.

    Returns a list of rows with the indice of the input letters
    if they were encrypted.
    The list will be in the format
    [[index1, index2, ...], [index3, index4, ...], ...]
    with 'key' elements

    Parameters
    ----------
    inp: str
        The input string
    key: int
        The key to en / decrypt
    """
    length = len(inp)
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


def encrypt(inp: str, key: int) -> str:
    """
    Encrypts a given input with the rail fence cipher and a provided key

    Parameters
    ----------
    inp: str
        The input string
    key: int
        The key to encrypt
    """
    inp = inp.strip()
    indice = _get_indices(inp, key)
    ret = ""
    for row in indice:
        for index in row:
            ret += inp[index]
    return ret


def decrypt(inp: str, key: int) -> str:
    """
    Decrypts a given input with the rail fence cipher and a provided key

    Parameters
    ----------
    inp: str
        The input string
    key: int
        The key to decrypt
    """
    inp = inp.strip()
    indice = _get_indices(inp, key)
    all_indice = []
    for x in indice:
        all_indice += x
    ret = ""
    for i in range(len(inp)):
        ret += inp[all_indice.index(i)]
    return ret

print(encrypt("12345678", 3))
