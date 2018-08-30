import pytest
import string
from hypothesis import given
from hypothesis.strategies import text, data

from cipy.ciphers.morse import *

@given(data=data())
def test_inversion_morse(data, morse_letters):
    msg = data.draw(text(alphabet=morse_letters, min_size=1))
    assert decrypt(encrypt(msg)) == msg
