import unittest
from exemple_doctest import factorielle


class Factorielle(unittest.TestCase):
    def test_factorielle_n_float(self):
        with self.assertRaises(ValueError):
            factorielle(1.0)

    def test_factorielle_n_trop_grand(self):
        with self.assertRaises(OverflowError):
            factorielle(1e300)

    def test_factorielle_n_negatif(self):
        with self.assertRaises(ValueError):
            factorielle(-1)

    def test_factorielle_n_positif(self):
        self.assertEqual(factorielle(4), 24)

    def test_factorielle_0(self):
        self.assertEqual(factorielle(0), 1)

    def test_factorielle_on_list(self):
        self.assertListEqual(
            [factorielle(n) for n in range(5)],
            [1, 1, 2, 6, 24])


if __name__ == "__main__":
    unittest.main()  # main est un point d’entrée qui 
    # determine toutes les classes ou il y a des tests
    # On lance le fichier avec python3 test.py —-verbose

# Si on enleve le main alors on peut lancer les 
# tests en faisant : python3 -m unittest test.py -v

# python3 -m unittest coverage run -m unittest test.py
# coverage html
