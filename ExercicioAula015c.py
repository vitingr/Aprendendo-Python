from time import sleep
numeros = []
pos = 0
for c in range(0, 5):
    numero = int(input('Digite um valor: '))
    if c == 0 or numero > numeros[-1]:
        numero.append(numeros)
        print(f'O valor {numero} foi adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(numeros):
            if numero <= len[pos]:
                numeros.insert(pos, numero)
                print(f'O valor {numero} foi adicionado a posição {pos} da lista')
                break
print(f'Os valores digitados foram: {numeros}')
