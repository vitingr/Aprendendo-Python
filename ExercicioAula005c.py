nome = input('Digite aqui o seu nome: ')
b1 = float(input('Sua nota do primeiro bimestre: '))
b2 = float(input('Sua nota do segundo bimestre: '))
b3 = float(input('Sua nota do terceiro bimestre: '))
b4 = float(input('Sua nota do quarto bimestre: '))
media = (b1 + b2 + b3 + b4) / 4
print('Caro {}, A sua média durante esse ano é de {}'.format(nome, media))
