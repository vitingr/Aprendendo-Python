par = list()
impar = list()
for c in range(1, 8):
    numero = int(input(f'Digite o {c}o Valor: '))
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
print(' '*30)
print('Você digitou um total de 7 valores.')
par.sort()
print(f'Os valores {par} são pares.')
impar.sort()
print(f'Os valores {impar} são ímpares.')
