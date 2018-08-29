import pytest
from hypothesis import given
from hypothesis.strategies import text

from cipy.ciphers.francis_bacon import *

@given(text(alphabet=LETTERS_LONG))
def test_inversion_francis_bacon(s):
    assert decrypt(encrypt(s)) == s

@given(text(alphabet=LETTERS_SHORT))
def test_inversion_francis_bacon_short(s):
    assert decrypt(encrypt(s, short=True), short=True) == s
