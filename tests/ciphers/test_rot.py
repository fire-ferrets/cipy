import pytest
import string
from hypothesis import given
from hypothesis.strategies import text, data

from cipy.ciphers.rot import *

@given(data=data())
def test_inversion_rot(data, ascii_low):
    msg = data.draw(text(alphabet=ascii_low))
    assert decrypt(encrypt(msg, 13), 13) == msg
