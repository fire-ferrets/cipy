import pytest
import string
from hypothesis import given
from hypothesis.strategies import text

from cipy.ciphers.morse import *

ALPHABET = "".join((string.ascii_uppercase, string.digits, " "))
@given(text(alphabet=ALPHABET, min_size=1))
def test_inversion_morse(s):
    assert decrypt(encrypt(s)) == s
