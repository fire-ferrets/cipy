import pytest
import string
from hypothesis import given
from hypothesis.strategies import text, data

from cipy.ciphers.vigenere import *

@given(data=data())
def test_inversion_vigenere(data, ascii_upper):
    msg = data.draw(text(alphabet=ascii_upper, min_size=9))
    assert decrypt(encrypt(msg, "cashmoney"), "cashmoney") == msg
