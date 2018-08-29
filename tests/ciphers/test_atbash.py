import pytest
from hypothesis import given
from hypothesis.strategies import text

from cipy.ciphers.atbash import *

@given(text(alphabet=ALPHABET, min_size=1))
def test_inversion_atbash(s):
    assert decrypt(encrypt(s)) == s
