from random import randint
from time import sleep
lista = list()


def sorteio(lista):
    print(f'Sorteando os números da lista: ', end='')
    for cont in range(0, 5):
        n = int(randint(0, 20))
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.3)
    print(' Pronto!')


def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'Somandos os valores pares de {lista}, obtemos o resultado {soma}')


numeros = lista
sorteio(numeros)
somaPar(numeros)
