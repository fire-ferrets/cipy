import pytest
import string
from hypothesis import given
from hypothesis.strategies import text

from cipy.ciphers.rail_fence import *

ALPHABET = string.ascii_letters
@given(text(alphabet=ALPHABET, min_size=5))
def test_inversion_rail_fence(s):
    assert decrypt(encrypt(s,3), 3) == s
