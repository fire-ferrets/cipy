import pytest
import string
from hypothesis import given
from hypothesis.strategies import text, data

from cipy.ciphers.ascii import *

@given(data=data())
def test_inversion_ascii(data, ascii_letters):
    msg = data.draw(text(alphabet=ascii_letters, min_size=1))
    assert decrypt(encrypt(msg)) == msg
