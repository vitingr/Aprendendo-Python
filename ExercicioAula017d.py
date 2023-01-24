matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for a in range(0, 3):
    for b in range(0, 3):
        matriz[a][b] = int(input(f'Digite um valor para [{a}, {b}]: '))
print(matriz)
for a in range(0, 3):
    for b in range(0, 3):
        print(f'[{matriz[a][b]:^5}]', end='')
    print()