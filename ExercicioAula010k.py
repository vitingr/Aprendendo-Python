from random import choice
pedra = 'Stone'
papel = 'Paper'
tesoura = 'Scissor'
print('{:=^40}'.format('\033[1;33mJogo do PPT\033[m'))
print(''*30)
print('Você deve escolher entre Pedra, Papel e Tesoura, e o vencedor será informado')
print('Papel > Pedra')
print('Pedra > Tesoura')
print('Tesoura > Papel')
print('' * 30)
print('Escolha o que você vai jogar.')
print('''
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
''')
opcao1 = int(input('Sua opção: '))
if opcao1 == 1:
    ppt = [pedra, papel, tesoura]
    jogada = choice(ppt)
    if jogada == 'Stone':
        print('A máquina jogou {}. Empate'.format('Pedra'))
    elif jogada == 'Paper':
        print('A máquina jogou {}. Que pena, Você perdeu!'.format('Papel'))
    elif jogada == 'Scissor':
        print('A máquina jogou {}. Parabéns, você venceu!'.format('Tesoura'))
if opcao1 == 2:
    ppt = [pedra, papel, tesoura]
    jogada = choice(ppt)
    if jogada == 'Stone':
        print('A máquina jogou {}. Parabéns, Você venceu!'.format('Pedra'))
    elif jogada == 'Paper':
        print('A máquina jogou {}. Empate'.format('Papel'))
    elif jogada == 'Scissor':
        print('A máquina jogou {}. Que pena, Você perdeu!'.format('Tesoura'))
if opcao1 == 3:
    ppt = [pedra, papel, tesoura]
    jogada = choice(ppt)
    if jogada == 'Stone':
        print('A máquina jogou {}. Que pena, você perdeu!'.format('Pedra'))
    elif jogada == 'Paper':
        print('A máquina jogou {}. Parabéns, Você venceu!'.format('Papel'))
    elif jogada == 'Scissor':
        print('A máquina jogou {}. Empate'.format('Tesoura'))
