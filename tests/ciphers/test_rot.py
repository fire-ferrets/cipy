import pytest
import string
from hypothesis import given
from hypothesis.strategies import text

from cipy.ciphers.rot import *

ALPHABET = string.ascii_lowercase
@given(text(alphabet=ALPHABET))
def test_inversion_rot(s):
    assert decrypt(encrypt(s, 13), 13) == s
