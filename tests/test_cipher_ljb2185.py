import pytest

from cipher_ljb2185 import cipher_ljb2185

def test_cipher_ljb2185():
    examples = [
        ('word', 'xpse'),
        ('single', 'tjohmf'),
        ('Random', 'Sboepn')]
    for example, expected in examples:
        actual = cipher_ljb2185(example,1)
        assert actual == expected

test_cipher_ljb2185()