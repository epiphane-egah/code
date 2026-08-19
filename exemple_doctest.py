# Doctest : exemple avec la fonction factorielle
import math


def factorielle(n: int) -> int:
    """Return the factorial of n, an exact integer >=0.
   >>> factorielle(3)
   6
   >>> [factorielle(n) for n in range(5)]
   [1, 1, 2, 6, 24]
   >>> factorielle(-1)
   Traceback (most recent call last):
               ...
   ValueError: n can't be negative
   >>> factorielle(1e300)
   Traceback (most recent call last):
               ...
   OverflowError: n value to large
   >>> factorielle(3.1)
   Traceback (most recent call last):
               ...
   ValueError: n must be exact integer, not float


   Args:
       n (int) : the number which factorial we want to compute

   Returns:
       int : the factorial of n

   """
    if n == 0:
        return 1
    elif math.floor(n) != n:
        raise ValueError('n must be exact integer, not float')
    elif n + 1 == n:
        raise OverflowError("n value to large")
    elif n > 0:
        return n*factorielle(n-1)
    else:
        raise ValueError("n can't be negative")


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)


# python test.py -v
# Ou on enlève la partie if name == main, et on lance les tests avec python -m doctest -v test.py
# Ou on met la docstring dans un fichier txt et on lance avec doctest.testfile(‘test.txt’) 