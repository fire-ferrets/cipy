"""
Morse cipher

Allows you to encrypt and decrypt Morse code
"""
TEXT_TO_MORSE = {
    "A": "10",
    "B": "0111",
    "C": "0101",
    "D": "011",
    "E": "1",
    "F": "1101",
    "G": "001",
    "H": "1111",
    "I": "11",
    "J": "1000",
    "K": "010",
    "L": "1011",
    "M": "00",
    "N": "01",
    "O": "000",
    "P": "1001",
    "Q": "0010",
    "R": "101",
    "S": "111",
    "T": "0",
    "U": "110",
    "V": "1110",
    "W": "100",
    "X": "0110",
    "Y": "0100",
    "Z": "0011",
    "1": "10000",
    "2": "11000",
    "3": "11100",
    "4": "11110",
    "5": "11111",
    "6": "01111",
    "7": "00111",
    "8": "00011",
    "9": "00001",
    "0": "00000",
    " ": "2"
}

MORSE_TO_TEXT = {
    "10": "A",
    "0111": "B",
    "0101": "C",
    "011": "D",
    "1": "E",
    "1101": "F",
    "001": "G",
    "1111": "H",
    "11": "I",
    "1000": "J",
    "010": "K",
    "1011": "L",
    "00": "M",
    "01": "N",
    "000": "O",
    "1001": "P",
    "0010": "Q",
    "101": "R",
    "111": "S",
    "0": "T",
    "110": "U",
    "1110": "V",
    "100": "W",
    "0110": "X",
    "0100": "Y",
    "0011": "Z",
    "10000": "1",
    "11000": "2",
    "11100": "3",
    "11110": "4",
    "11111": "5",
    "01111": "6",
    "00111": "7",
    "00011": "8",
    "00001": "9",
    "00000": "0",
    "2": " "
}


def encrypt(inp: str, dot: str = ".", dash: str = "-", space: str = "/") -> str:
    """
    Encrypts a given input with the Morse cipher

    Parameters
    ----------
    inp: str
        The text you want to encrypt
    dot: str
        The character you want to represent a dot
    dash: str
        The character you want to represent a dash
    space: str
        The character you want to represent a space
    """
    letters = [TEXT_TO_MORSE[x].replace("0", dash).replace("1", dot).replace("2", space) for x in inp.upper()]
    return " ".join(letters)


def decrypt(inp: str, dot: str = ".", dash: str = "-", space: str = "/") -> str:
    """
    Encrypts a given input with the Morse cipher

    Parameters
    ----------
    inp: str
        The text you want to encrypt
    dot: str
        The character you want to represent a dot
    dash: str
        The character you want to represent a dash
    space: str
        The character you want to represent a space
    """
    letters = [MORSE_TO_TEXT[x.replace(dash, "0").replace(dot, "1").replace(space, "2")] for x in inp.split(" ")]
    return "".join(letters)