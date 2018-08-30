import pytest
import string
import numpy as np
from hypothesis import given
from hypothesis.strategies import text

from cipy.ciphers.hill import *

ALPHABET = string.ascii_letters
@given(s=text(alphabet=ALPHABET))
def test_inversion_hill(s):
    KEY = np.random.randint(low=len(s), size=(4,4))
    ALPHABET = string.ascii_letters
    assert decrypt(encrypt(s, KEY, ALPHABET), KEY, ALPHABET) == s

