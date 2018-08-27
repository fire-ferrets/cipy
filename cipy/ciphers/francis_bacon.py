"""
Encrypts and decrypts text with the Francis Bacon cipher
"""
LETTERS_LONG = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LETTERS_SHORT = "ABCDEFGHIKLMNOPQRSTUWXYZ"


def decrypt(inp: str, a: str = "A", b: str = "B", short: bool = False) -> str:
    """
    Decrypts a given message
    Parameters:
        inp     : the string you want to decrypt
        a       : the character you want to use for "A"s
        b       : the character you want to use for "B"s
        short   : True if you want to use the 24 character alphabet, otherwise
                  you use the 26 letter alphabet. Defaults to False.
    """
    if len(inp) % 5 != 0:
        print(f"Your input must have a length of a multiple of 5.\n Your length: {len(inp)}")
        return None

    # turning the input into binary data
    binary_input = inp.replace(a, "0").replace(b, "1")
    # splitting the input into blocks of length 5
    splits = [binary_input[i:i+5] for i in range(0, len(binary_input), 5)]
    # calculating integer values from binary blocks
    values = [int(x, 2) for x in splits]
    result_long = "".join(LETTERS_LONG[x] for x in values)
    result_short = "".join(LETTERS_SHORT[x] for x in values)
    if short:
        return result_short
    return result_long


def encrypt(inp: str, a: str = "A", b: str = "B", short: bool = False) -> str:
    """
    Encrypts a given message
    Parameters:
        inp     : the string you want to encrypt
        a       : the character you want to use for "A"s
        b       : the character you want to use for "B"s
        short   : True if you want to use the 24 character alphabet, otherwise
                  you use the 26 letter alphabet. Defaults to False.
    """
    inp = inp.upper()
    if short:
        bin_values = [bin(LETTERS_SHORT.index(x))[2:] for x in inp]
    else:
        bin_values = [bin(LETTERS_LONG.index(x))[2:] for x in inp]
    # fill the strings until theyre of length 5
    # for x in range(len(bin_values)):
    #     bin_values[x] = "0" * (5 - len(bin_values[x])) + bin_values[x]
    for i, x in enumerate(bin_values):
        bin_values[i] = "0" * (5 - len(x)) + x
    ret = "".join(bin_values).replace("0", a).replace("1", b)
    return ret
