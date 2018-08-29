import pytest
import string
from hypothesis import given
from hypothesis.strategies import text

from cipy.ciphers.vigenere import *

ALPHABET = string.ascii_uppercase
@given(text(alphabet=ALPHABET, min_size=9))
def test_inversion_vigenere(s):
    assert decrypt(encrypt(s, "cashmoney"), "cashmoney") == s
