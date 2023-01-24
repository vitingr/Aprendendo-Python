algo = str(input('Digite Algo: ')).strip().upper()
print('A letra A, aparece nesssa frase {} vezes.'.format(algo.count('A')))
print('A letra A aparece pela primeira vez na posiçao {}'.format(algo.find('A')+1))
print('A letra A aparece pela última vez na posição {}'.format(algo.rfind('A')))
