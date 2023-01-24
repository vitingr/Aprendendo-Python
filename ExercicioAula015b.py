from time import sleep
numeros = []
total = 0
while True:
    numero = int(input('Digite um número: '))
    if numero not in numeros:
        numeros.append(numero)
        total += 1
        print('Checando...')
        sleep(2)
        print('\033[92mNúmero adicionado com sucesso!\033[m')
    else:
        print('Checando...')
        sleep(2)
        print('\033[91mValor inválido, não foi possível adicionar!\033[m')
    c = str(input('Deseja digitar outro número? [S/N]: ')).upper().strip()
    if c in 'Nn':
        break
print(' '*30)
print('='*30)
print(' '*30)
print(f'Ao todo, você digitou um total de {total} números, são eles {numeros}')
print(' '*30)
print('='*30)

