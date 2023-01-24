from random import randint
number = randint(0, 10)
numero = 0
print('Eu pensei em um número, tente adivinhar: ')
acertou = False
while not acertou:
    palpite = int(input('Qual seu palpite? '))
    if palpite == number:
        acertou = True
    else:
        print('Que pena, você errou! Tente novamente')
print('Parabéns, você acertou!')