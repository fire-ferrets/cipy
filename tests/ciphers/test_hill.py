import pytest
import string
from hypothesis import given
from hypothesis.strategies import text, data

from cipy.ciphers.hill import *

@given(data=data())
def test_inversion_hill(data, ascii_letters, matrix):
    msg = data.draw(text(alphabet=ascii_letters, min_size=3, max_size=3))
    assert decrypt(encrypt(msg, matrix, ascii_letters), matrix, ascii_letters) == msg

