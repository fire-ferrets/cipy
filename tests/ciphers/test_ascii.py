import pytest
import string
from hypothesis import given
from hypothesis.strategies import text

from cipy.ciphers.ascii import *

ALPHABET = string.ascii_letters

@given(text(alphabet=ALPHABET, min_size=1))
def test_inversion_ascii(s):
    assert decrypt(encrypt(s)) == s
