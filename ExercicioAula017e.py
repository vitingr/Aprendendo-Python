# a = linha
# b = coluna
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = maior = somacoluna = 0
for a in range(0, 3):
    for b in range (0, 3):
        matriz[a][b] = int(input(f'Digite um valor para [{a}, {b}]: '))
print(matriz)
for a in range(0, 3):
    for b in range(0, 3):
        print(f'[{matriz[a][b]:^5}]', end='')
        if matriz[a][b] % 2 == 0:
            pares += matriz[a][b]
    print()
for a in range(0, 3):
    somacoluna += matriz[a][2]
for b in range(0, 3):
    if b == 0:
        maior = matriz[1][b]
    elif matriz[1][b] > maior:
        maior = matriz[1][b]
print(' '*30)
print(f'A soma dos valores pares digitados é igual a {pares}')
print(f'A soma dos valores presentes na terceira coluna é igual a {somacoluna}')
print(f'O maior valor presente na segunda linha, é o valor {maior}')
