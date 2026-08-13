import asyncio
from asyncio import run, gather, create_task, ensure_future
# Concurrence avec les coroutines

# Un processus est un ensemble de thread

# Un thread est un ensemble de coroutine

# Une coroutine est une fonction avec
# plusieurs points d'entrée et de sortie
# Une sous coroutine


async def coroutine1():
    print("Je suis l'entrée n°1 de la coroutine1")
    print("Je suis la sortie n°1 de la coroutine1")
    await asyncio.sleep(2)
    print("Je suis l'entrée n°2 de la coroutine1")
    print("Je suis la sortie n°2 de la coroutine1")
    await asyncio.sleep(4)
    print("Je suis l'entrée n°3 de la coroutine1")
    print("Je suis la sortie n°3 de la coroutine1")


async def coroutine2():
    print("Je suis l'entrée n°1 de la coroutine2")
    print("Je suis la sortie n°1 de la coroutine2")
    await asyncio.sleep(2)
    print("Je suis l'entrée n°2 de la coroutine2")
    print("Je suis la sortie n°2 de la coroutine2")
    await asyncio.sleep(4)
    print("Je suis l'entrée n°3 de la coroutine2")
    print("Je suis la sortie n°3 de la coroutine2")

# objet coroutine
run(coroutine1())  # await coroutine1()

print("-----------------------------------------------------")
print("-----------------------------------------------------")


async def main():
    await gather(coroutine1(), coroutine2())
run(main())

print("-----------------------------------------------------")
print("-----------------------------------------------------")


async def main_task():
    task1 = create_task(coroutine1())
    task2 = create_task(coroutine2())

    await task1
    await task2
run(main_task())

print("-----------------------------------------------------")
print("-----------------------------------------------------")


async def main_future():
    future1 = ensure_future(coroutine1())
    future2 = ensure_future(coroutine2())

    await future1
    await future2
run(main_future())
# tâche attentable (coroutine, tâche et future)