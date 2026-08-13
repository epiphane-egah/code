from threading import Thread
from multiprocessing import Pool
from random import randint
from typing import List
import time


def factoriel(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n*factoriel(n-1) 


# séquentiel
def sequentiel(liste_params: List):
    list_resultat = []
    for elem in liste_params:
        list_resultat.append(factoriel(elem))
    return list_resultat


# parallèle
# avec le multithreading


def multithreading(liste_params: List):
    liste_threads: List = []
    liste_result: List = [None] * len(liste_params)

    def worker(indice, param):
        liste_result[indice] = factoriel(param)
    for indice, _ in enumerate(range(len(liste_params))):
        t = Thread(target=worker, args=(indice, liste_params[indice]))
        t.start()
        liste_threads.append(t)

    for t in liste_threads:
        t.join()

    return liste_result
# from concurrent.futures import ThreadPoolExecutor
# with ThreadPoolExecutor(max_workers=4) as executor:
#     future = executor.submit(ma_fonction, arg1, arg2)
#     resultat = future.result()

# avec le multiprocessing


def multiprocessing(liste_params: List):
    with Pool(4) as coeurs:
        liste_result = coeurs.map(func=factoriel, iterable=liste_params)
    return liste_result
# from concurrent.futures import ProcessPoolExecutor
# with ProcessPoolExecutor(max_workers=4) as executor:
#     future = executor.submit(calcul_lourd, arg1)
#     resultat = future.result()


if __name__ == '__main__':
    liste_params = [randint(3, 320) for _ in range(5)]

    t1 = time.time()
    print(sequentiel(liste_params))
    t2 = time.time()
    print(f"Le temps d'execution est de {t2-t1} secondes")

    t1 = time.time()
    print(multithreading(liste_params))
    t2 = time.time()
    print(f"Le temps d'execution est de {t2-t1} secondes")

    t1 = time.time()
    print(multiprocessing(liste_params))
    t2 = time.time()
    print(f"Le temps d'execution est de {t2-t1} secondes")