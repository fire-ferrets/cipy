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

MORSE_TO_TEXT = {k: v for v, k in TEXT_TO_MORSE.items()}


def encrypt(msg: str, dot: str = ".", dash: str = "-", space: str = "/") -> str:
    """
    Encrypt a message using Morse code

    Parameters
    ----------
    msg: str
        The text you want to encrypt
    dot: str
        The character you want to represent a dot
    dash: str
        The character you want to represent a dash
    space: str
        The character you want to represent a space
    """
    letters = [TEXT_TO_MORSE[x] for x in msg.upper()]
    return " ".join(letters).replace("0", dash).replace("1", dot).replace("2", space)


def decrypt(msg: str, dot: str = ".", dash: str = "-", space: str = "/") -> str:
    """
    Decrypt a message that is written in Morse code

    Parameters
    ----------
    msg: str
        The message you want to encrypt
    dot: str
        The character you want to represent a dot
    dash: str
        The character you want to represent a dash
    space: str
        The character you want to represent a space
    """
    msg = msg.replace(dash, "0").replace(dot, "1").replace(space, "2")
    letters = [MORSE_TO_TEXT[x] for x in msg.split(" ")]
    return "".join(letters)
