import emoji
import math
nome = input('Nome do aluno: ')
print(emoji.emojize('A seguir, informe as notas do aluno em seus respectivos semestres :books:', use_aliases=True))
b1 = float(input('Nota do 1 Bimestre: '))
b2 = float(input('Nota do 2 Bimestre: '))
b3 = float(input('Nota do 3 Bimestre: '))
b4 = float(input('Nota do 4 Bimestre: '))
total = (b1 + b2 + b3 + b4) / 4
media = math.floor(total)
print('Durante os 4 bimestres, o aluno obteve as notas de {}, {}, {}, {}. Consequentemente sua média será de {}.'
      .format(b1, b2, b3, b4, media))
