import pytest
import string
from hypothesis import given
from hypothesis.strategies import text, data

from cipy.ciphers.rail_fence import *

@given(data=data())
def test_inversion_rail_fence(data, ascii_letters):
    msg = data.draw(text(alphabet=ascii_letters, min_size=5))
    assert decrypt(encrypt(msg, 3), 3) == msg
