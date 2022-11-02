import pytest

def test_cipher():
    examples = [
        ('word', 'xpse'),
        ('single', 'tjohmf'),
        ('Random', 'Sboepn')]
    for example, expected in examples:
        actual = cipher(example,1)
        assert actual == expected

test_cipher()