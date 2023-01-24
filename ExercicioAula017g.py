from random import randint
from time import sleep
print('='*40)
print('\033[92mJoga na Mega-Sena\033[m')
print('='*40)
total = 1
numeros = list()
save = list()
qtd = int(input('Digite quantos jogos você quer que eu sorteie? '))
while total <= qtd:
    cont = 0
    while True:
        num = (randint(1, 60))
        if num not in save:
            save.append(num)
            cont += 1
        if cont >= 6:
            break
    save.sort()
    numeros.append(save[:])
    save.clear()
    total += 1
print(f'-=-=- Sorteando {qtd} jogos, Aguarde... -=-=-')
sleep(1)
for a, b in enumerate(numeros):
    sleep(2)
    print(f'Jogo {a + 1}: {b}')
