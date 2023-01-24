from random import randint
numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    print(f'\033[92mNúmero Adicionado com Sucesso...\033[m')
    c = str(input('Deseja continuar? [S/N]: '))
    if c in 'Nn':
        break
print(f'Você digitou um total de {len(numeros)} números')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {numeros}')
n = randint(0, 10)
if n in numeros:
    print(f'O valor {n} foi encontrado na lista')
else:
    print(f'O valor {n} não foi encontrado na lista')