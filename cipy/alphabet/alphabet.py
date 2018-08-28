"""
This file provides some basic alphabets for ciphering
"""

import itertools

class Alphabet():
    def __init__(self, alphabet):
        self.alphabet = alphabet
        self.length = len(alphabet)
        self._numbers_to_alphabet = dict(enumerate(self.alphabet))
        self._alphabet_to_numbers = dict((v, k) for k,v in self._numbers_to_alphabet)

    def __len__(self):
        return len(self.length)

    def __len_hint__(self):
        return len(self.length)

    def __getitem__(self, key):
        if key in self._numbers_to_alphabet:
            return self._numbers_to_alphabet[key]
        elif key in self._alphabet_to_numbers:
            return self._alphabet_to_numbers[key]

    def __missing__(self,key, value):
        raise KeyError("Key not found in Alphabet")

    def __iter__(self):
        iterable = itertools.chain(
                self._numbers_to_alphabet.keys(),
                self._alphabet_to_numbers.keys())
        return iterable

    def __reversed__(self):
        iterable = itertoo.chain(
                reversed(self._numbers_to_alphabet.keys()),
                reversed(self._alphabet_to_numbers.keys())
                )
        return iterable

    def __contains__(self, item):
        if item in self._numbers_to_alphabet.keys():
            return True
        elif item in self._alphabet_to_numbers.keys():
            return True
        else:
            return False
