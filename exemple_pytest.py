# Les tests réalisés avec unittest sont compatible avec pytest

import pytest

# my own module
from exemple_doctest import factorielle


def test_factorielle_n_float():
   with pytest.raises(ValueError):
       factorielle(-1)


def test_factorielle_n_trop_grand():
   with pytest.raises(OverflowError):
       factorielle(1e300)


def test_factorielle_n_negatif():
   with pytest.raises(ValueError):
       factorielle(-1)


def test_factorielle_n_positif():
   assert factorielle(4) == 24


def test_factorielle_0():
   assert factorielle(0) == 1


def test_factorielle_on_list():
   assert [factorielle(n) for n in range(5)] == [1, 1, 2, 6, 24]

# python3 -m pytest test.py -v –html=file.html

# Les fixtures avec pytest


class Bank:
    a = 3


@pytest.fixture
def account():
    user = Bank()
    return user


def test_account(account):
    assert account.a == 3
