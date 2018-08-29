"""
The Alphabet class provides a general framework to embed alphabets

It takes a string of the chosen alphabet as attribute. This provides
the encryption and decryption functions for the ciphers with a performance
boost.
"""


class Alphabet():
    def __init__(self, alphabet):
        """
        Initialise an Alphabet

        Attributes
        ----------
        alphabet : str
            The alphabet string
        """
        self.alphabet = alphabet
        self._length = len(alphabet)
        self._numbers_to_alphabet = dict(enumerate(self.alphabet))
        self._alphabet_to_numbers = dict((v, k) for k,v in self._numbers_to_alphabet.items())

    def __repr__(self):
        return self.alphabet

    def __len__(self):
        return self._length

    def __len_hint__(self):
        return self._length

    def __getitem__(self, key):
        if key in self._numbers_to_alphabet:
            return self._numbers_to_alphabet[key]
        elif key in self._alphabet_to_numbers:
            return self._alphabet_to_numbers[key]

    def __missing__(self,key, value):
        raise KeyError("Key not found in Alphabet")

    def __iter__(self):
        return self._alphabet_to_numbers.items()

    def __reversed__(self):
        return reversed(self._alphabet_to_numbers.keys())

    def __contains__(self, item):
        if item in self._alphabet_to_numbers.keys():
            return True
        else:
            return False
