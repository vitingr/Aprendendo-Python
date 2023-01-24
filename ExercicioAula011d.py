from random import randint
soma = 0
cont = 0
for c in range(1, 501, 2):
     if c % 3 == 0:
          cont += c
          soma += 1
print('O somatório dos {} valores solicitados é igual a {}'.format(cont, soma))
