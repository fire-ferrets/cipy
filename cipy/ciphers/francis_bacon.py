"""
Encrypts and decrypts text with the Francis Bacon cipher
"""
LETTERS_LONG = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LETTERS_SHORT = "ABCDEFGHIKLMNOPQRSTUWXYZ"


def decrypt(msg: str, a: str = "A", b: str = "B", short: bool = False) -> str:
    """
    Decrypt a message that is encrypted using a Francis Bacon cipher

    Parameters
    ----------
    msg: str
        The message you want to decrypt
    a: str
        The character you want to use as the "A"
    b: str
        The character you want to use as the "B"
    short: bool
        Decides whether or not you want to use the 24 letter alphabet.
    """
    if len(msg) % 5 != 0:
        return None

    # turning the msgut into binary data
    binary_msgut = msg.replace(a, "0").replace(b, "1")
    # splitting the msgut into blocks of length 5
    splits = [binary_msgut[i:i+5] for i in range(0, len(binary_input), 5)]
    # calculating integer values from binary blocks
    values = [int(x, 2) for x in splits]
    if short:
        result = "".join(LETTERS_SHORT[x] for x in values)
    else:
        result = "".join(LETTERS_LONG[x] for x in values)
    return result


def encrypt(msg: str, a: str = "A", b: str = "B", short: bool = False) -> str:
    """
    Encrypt a message using a Francis Bacon cipher

    Parameters
    ----------
    msg: str
        The message you want to encrypt
    a: str
        The character you want to use as the "A"
    b: str
        The character you want to use as the "B"
    short: bool
        Decides whether or not you want to use the 24 letter alphabet.
    """
    msg = msg.upper()
    if short:
        bin_values = [bin(LETTERS_SHORT.index(x))[2:] for x in msg]
    else:
        bin_values = [bin(LETTERS_LONG.index(x))[2:] for x in msg]
    # fill the strings until theyre of length 5
    for i, x in enumerate(bin_values):
        bin_values[i] = "0" * (5 - len(x)) + x
    ret = "".join(bin_values).replace("0", a).replace("1", b)
    return ret
