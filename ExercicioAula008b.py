from random import randint
from time import sleep
print('='*30)
print('\033[1;36mBem-Vindo ao Jogo da Advinhação!\033[m')
print(''*30)
print('Para jogar é muito simples, eu irei pensar em um número ')
print('E você deverá advinhar em qual número eu pensei, Vamos Lá?')
print(''*30)
print('='*30)
number = randint(1, 5)
chance = int(input('Tente acertar qual número eu pensei: '))
print('Processando...')
sleep(3)
if chance == number:
    print('Parabéns! Você acertou o número.')
else:
    print('Que pena, você não acertou... O número correto era {}!'.format(number))
