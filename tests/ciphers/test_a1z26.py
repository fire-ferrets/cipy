import pytest
from hypothesis import given
from hypothesis.strategies import text

from cipy.ciphers.a1z26 import *

@given(text(alphabet=ALPHABET, min_size=1))
def test_inversion_a1z26(s):
    assert decrypt(encrypt(s)) == s
