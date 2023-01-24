numeros = list()
par = list()
impar = list()
total = 0
while True:
    numero = int(input('Digite um valor: '))
    print('\033[92mNúmero Adicionado com Sucesso!\033[m')
    print(' '*30)
    numeros.append(numero)
    if numero % 2 == 0:
        par.append(numero)
        total += 1
    else:
        impar.append(numero)
        total += 1
    c = str(input('Deseja continuar? [S/N] '))
    print(' '*30)
    if c in 'Nn':
        break
numeros.sort()
print(' '*30)
print('='*30)
print(f'Você digitou um total de {total} números')
print(f'Os números digitados foram {numeros}')
print(f'E os valores {par} são números pares')
print(f'E os valores {impar} são números impares')
print(' '*30)
print('='*30)
