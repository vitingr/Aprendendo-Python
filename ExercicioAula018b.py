from random import randint
from time import sleep
from operator import itemgetter
jogadas = dict()
ranking = list()
jogador1 = int(randint(1, 6))
jogador2 = int(randint(1, 6))
jogador3 = int(randint(1, 6))
jogador4 = int(randint(1, 6))
jogador5 = int(randint(1, 6))
jogadas['Jogador 1'] = jogador1
jogadas['Jogador 2'] = jogador2
jogadas['Jogador 3'] = jogador3
jogadas['Jogador 4'] = jogador4
jogadas['Jogador 5'] = jogador5
print(' ' * 40)
print('Valores sorteados: ')
for a, b in jogadas.items():
    print(f'O jogador {a} tirou o valor {b}')
    sleep(1)
print(' ' * 40)
print('-=' * 40)
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print(f'          == \033[92mRanking dos Jogadores\033[m ==')
for c, d in enumerate(ranking):
    print(f'{c + 1:>10}º Lugar: {d[0]} com {d[1]} pontos')
print(' ' * 40)
print('-=' * 40)


